import Foundation

struct Square {
    let y: Int
    let x: Int
    let w: Int
}

enum SolveError: Error {
    case impossible
}

func solveWithRequired(N: Int, required: [Int]) throws -> (Int, [Square]) {
    guard N > 1 else { throw SolveError.impossible }

    for w in required {
        if w >= N || w <= 0 {
            throw SolveError.impossible
        }
    }

    var requiredCount: [Int: Int] = [:]
    var requiredArea = 0
    for w in required {
        requiredCount[w, default: 0] += 1
        requiredArea += w * w
    }

    let totalArea = N * N
    if requiredArea > totalArea {
        throw SolveError.impossible
    }

    var table = Array(repeating: Array(repeating: 0, count: N), count: N)
    var bestCount = Int.max
    var bestSolution: [Square] = []

    func findFree() -> (Int, Int)? {
        for y in 0..<N {
            for x in 0..<N {
                if table[y][x] == 0 { return (y, x) }
            }
        }
        return nil
    }

    func canPlace(_ y: Int, _ x: Int, _ w: Int) -> Bool {
        if y + w > N || x + w > N { return false }
        for i in y..<y+w {
            for j in x..<x+w {
                if table[i][j] != 0 { return false }
            }
        }
        return true
    }

    func fill(_ y: Int, _ x: Int, _ w: Int, _ color: Int) {
        for i in 0..<w {
            for j in 0..<w {
                table[y + i][x + j] = color
            }
        }
    }

    func backtrack(_ curK: Int,
                   _ emptyArea: Int,
                   _ requiredLeft: [Int: Int],
                   _ requiredAreaLeft: Int,
                   _ current: inout [Square]) {
        
        // Отсечение по количеству квадратов
        if curK >= bestCount { return }
        // Отчесение по оставшейся площади
        if requiredAreaLeft > emptyArea { return }

        guard let (y, x) = findFree() else {
            if requiredAreaLeft == 0 && curK < bestCount {
                bestCount = curK
                bestSolution = current
            }
            return
        }

        let maxW = min(N - y, N - x)

        // Отсечение по площади, если ее не хватает, чтобы покрыть остаток минимальным кол-вом квадратов
        if bestCount < Int.max {
            let remaining = bestCount - curK
            if remaining > 0 {
                let maxCover = Double(remaining) * Double(maxW) * Double(maxW)
                if Double(emptyArea) > maxCover {
                    return
                }
            }
        }

        for w in stride(from: maxW, through: 1, by: -1) {
            if !canPlace(y, x, w) { continue }

            var newReq = requiredLeft
            var newReqArea = requiredAreaLeft

            // Если текущий размер w есть в списке обязательных квадратов, уменьшаем счётчик и вычитаем его площадь
            if let cnt = newReq[w], cnt > 0 {
                newReq[w] = cnt - 1
                newReqArea -= w * w
            }

            
            fill(y, x, w, 1) // поставили квадрат
            current.append(Square(y: y+1, x: x+1, w: w)) // добавили в решение, но начало координат по ТЗ это (1, 1) => сдвиг

            backtrack(curK + 1,
                      emptyArea - w*w,
                      newReq,
                      newReqArea,
                      &current) // пытаемся построить размещение дальше

            current.removeLast() // откат
            fill(y, x, w, 0)
        }
    }

    
    var cur: [Square] = []
    backtrack(0, totalArea, requiredCount, requiredArea, &cur)

    if bestCount == Int.max {
        throw SolveError.impossible // не нашли решение
    }

    return (bestCount, bestSolution) // нашли решение
}


// generator
func generateSquareList(maxSize: Int,
                        allowDuplicates: Bool,
                        length: Int) -> [Int] {
    if maxSize <= 0 || length < 0 {
        return []
    }

    if !allowDuplicates && length > maxSize {
        return Array(1...maxSize)
    }

    if allowDuplicates {
        return (0..<length).map { _ in Int.random(in: 1...maxSize) }
    } else {
        var arr = Array(1...maxSize)
        arr.shuffle()
        return Array(arr.prefix(length))
    }
}

