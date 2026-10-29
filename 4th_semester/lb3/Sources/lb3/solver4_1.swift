// TODO: additionaly to add cursed & Z symbols proccessing + testing

func minErrorDist(_ cursed: [Int], _ s1: String, _ s2: String, _ replaceCost: Int, _ insertCost: Int, _ deleteCost: Int) -> (String, Int) {
    let m = s1.count
    let n = s2.count
    
    let cursedSet = Set(cursed) // уникальные индексы (0-based)
    let INF = Int.max / 2 // чтобы избежать переполнения при сложении
    
    // Переводим строки в массивы символов для удобного доступа по индексу
    let a = Array(s1)
    let b = Array(s2)
    

    // ОБРАБОТКА ПУСТЫХ СТРОК
    // Случай 1: первая строка пустая -> только вставки
    if m == 0 {
        var path = ""
        for _ in 0..<n {
            path.append("I")
        }
        return (path, n * insertCost)
    }

    // Случай 2: вторая строка пустая -> только удаления
    if n == 0 {
        var totalCost = 0
        var path = ""
        for i in 0..<m {
            // Проклятый символ (любой, включая Z) нельзя удалять
            if cursedSet.contains(i) {
                return ("", -1)
            }
            totalCost += deleteCost
            path.append("D")
        }
        return (path, totalCost)
    }
    
    
    // Создаём таблицу (m+1) x (n+1)
    var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
    
    // Базовый случай: пустая s1 -> s2 (только вставки) - всегда возможно
    for j in 0...n {
        dp[0][j] = j * insertCost
    }
    
    // Базовый случай: s1 -> пустая s2 (только удаления)
    // Проклятые элементы удалять нельзя -> ставим INF
    for i in 0...m {
        if i == 0 {
            dp[i][0] = 0
        } else if cursedSet.contains(i - 1) { // индекс в строке = i-1
            dp[i][0] = INF // нельзя удалить проклятый символ
        } else {
            dp[i][0] = dp[i-1][0] + deleteCost
        }
    }
    
    // Заполняем таблицу
    for i in 1...m {
        let isCursed = cursedSet.contains(i - 1) // текущий символ A[i-1]
        let isZ = a[i-1] == "Z"
        
        for j in 1...n {
            // 1. Удаление (Запрещено для всех проклятых)
            let del: Int
            if isCursed {
                del = INF
            } else {
                del = dp[i-1][j] + deleteCost
            }
            
            // 2. Вставка (всегда возможна)
            let ins = dp[i][j-1] + insertCost
            
            // 3. Замена/совпадение
            let rep: Int
            if a[i-1] == b[j-1] {
                rep = dp[i-1][j-1] // символы совпали
            } else {
                // Замена запрещена для проклятых (кроме Z)
                if isCursed && !isZ {
                    rep = INF
                } else {
                    rep = dp[i-1][j-1] + replaceCost
                }
            }
           
            // Берём минимум
            dp[i][j] = min(del, ins, rep)
        }
    }
    
//    for i in 0..<m {
//        print(dp[i])
//    }
    
    let cost = dp[m][n]
    
    // Если преобразование невозможно
    if cost >= INF {
        return ("", -1)
    }
    
    // Восстановление пути (обратный ход)
    var pathChars: [Character] = []
    var i = m
    var j = n
    
    // (i, j) -> string1: a[i-1], string2: b[i-1]
    
    while i > 0 || j > 0 {
        if i > 0 && (dp[i][j] == dp[i-1][j] + deleteCost) {
            pathChars.append("D")
            i -= 1
        } else if j > 0 && (dp[i][j] == dp[i][j-1] + insertCost) {
            pathChars.append("I")
            j -= 1
        } else {
            if a[i-1] != b[j-1] {
                pathChars.append("R")
            } else {
                pathChars.append("M") // nothing
            }
            i -= 1
            j -= 1
        }
    }
    
    return (String(pathChars.reversed()), cost)
}


func solve4_1() -> (String, Int) {
    
    // Чтение входных данных
    let costs = readLine()!.split(separator: " ").map { Int($0)! }
    let replaceCost = costs[0]
    let insertCost = costs[1]
    let deleteCost = costs[2]
    
    let s1 = readLine()!
    let s2 = readLine()!
    
    let cursed = readLine()!.split(separator: " ").map { Int($0)! }
    
    
    // Алгоритм
    let (path, cost) = minErrorDist(cursed, s1, s2, replaceCost, insertCost, deleteCost)
    
    print(cost)
    if cost != -1 {
        print(path)
    }
    
    return (path, cost)
}
