import Foundation

func isPrime(_ n: Int) -> Bool { // O(sqrt(n))
    if n < 2 { return false }
    if n == 2 { return true }
    let r = Int(Double(n).squareRoot())
    for i in 2...max(r, 2) {
        if n % i == 0 { return false }
    }
    return true
}

func findFreeCoords(_ table: [[Int]], _ startY: Int = 0) -> (Int, Int)? { // O(n^2)
    let n = table.count
    for y in startY..<n {
        for x in 0..<n {
            if table[y][x] == 0 {
                return (y, x)
            }
        }
    }
    return nil
}

func canPlace(_ table: [[Int]], _ y: Int, _ x: Int, _ w: Int) -> Bool { // O(w^2)
    let n = table.count
    if y + w > n || x + w > n { return false }
    for i in y..<y+w {
        for j in x..<x+w {
            if table[i][j] != 0 { return false }
        }
    }
    return true
}

func fill(_ table: inout [[Int]], _ y: Int, _ x: Int, _ w: Int, _ color: Int) { // O(w^2)
    for i in 0..<w {
        for j in 0..<w {
            table[y + i][x + j] = color
        }
    }
}

func getMinPrimeDiv(_ n: Int) -> Int { // O(sqrt(n))
    if n % 2 == 0 { return 2 }
    let r = Int(Double(n).squareRoot())
    if r >= 3 {
        for i in stride(from: 3, through: r, by: 2) {
            if n % i == 0 { return i }
        }
    }
    return n
}

func solve(_ N: Int) -> (Int, [[Int]]) {
    var best = (N * N, [[Int]]())
    var table = Array(repeating: Array(repeating: 0, count: N), count: N)

    func backtrack(_ curK: Int, _ curRes: inout [[Int]], _ startY: Int, _ emptyArea: Int) {
        // Отсечение по количеству квадратов
        if curK >= best.0 { return }

        guard let (y, x) = findFreeCoords(table, startY) else {
            // Нашли решение
            if curK < best.0 {
                best.0 = curK
                best.1 = curRes.map { $0 } // copying
            }
            return
        }

        // Отсечение по площади, если ее не хватает, чтобы покрыть остаток
        let maxW = min(N - y, N - x)
        let remainingSquares = best.0 - curK
        if emptyArea > remainingSquares * (maxW * maxW) {
            return
        }

        for w in stride(from: maxW, through: 1, by: -1) {
            if canPlace(table, y, x, w) {
                
                fill(&table, y, x, w, 1)
                curRes.append([y + 1, x + 1, w]) // поставили квадрат на поле

                backtrack(curK + 1, &curRes, y, emptyArea - w * w) // пытаемся достроить решение

                curRes.removeLast() // здесь окажемся в любом случае: если попытка неудачная или найдено решение (но не факт, что оптимальное)
                fill(&table, y, x, w, 0) // поэтому удаляем квадрат, чтобы проверить следующие w
            }
        }
    }

    // Case 1: N is even
    if N % 2 == 0 {
        let h = N / 2
        best.0 = 4
        best.1 = [
            [1, 1, h],
            [1, 1 + h, h],
            [1 + h, 1, h],
            [1 + h, 1 + h, h]
        ]
        return best
    }

    // Case 2: N is prime
    if isPrime(N) {
        let a = (N + 1) / 2
        let b = (N - 1) / 2

        fill(&table, 0, 0, a, 1)
        fill(&table, 0, a, b, 1)
        fill(&table, a, 0, b, 1)

        var curRes = [
            [1, 1, a],
            [a + 1, 1, b],
            [1, a + 1, b]
        ]
        
        let initialEmptyArea = N * N - (a * a + b * b + b * b) // выкидываем 1 большой a*a и 2 b*b по краям

        backtrack(3, &curRes, 0, initialEmptyArea)
        return best
    }

    // Case 3: N is composite
    let div = getMinPrimeDiv(N)
    let q = N / div
    
    // Решаем для меньшего размера div
    let smallerResult = solve(div)
    
    // Масштабируем решение
    var scaledSquares = [[Int]]()
    for square in smallerResult.1 {
        let y = square[0]
        let x = square[1]
        let w = square[2]
        
        let newY = (y - 1) * q + 1
        let newX = (x - 1) * q + 1
        let newW = w * q
        
        scaledSquares.append([newY, newX, newW])
    }
    
    best.0 = smallerResult.0
    best.1 = scaledSquares
    return best
}
