// TODO: additionaly to add cursed & Z symbols proccessing + testing


func minErrorDistOpt(_ cursed: [Int], _ s1: String, _ s2: String) -> Int {
    let m = s1.count
    let n = s2.count
    
    // ОБРАБОТКА ПУСТЫХ СТРОК
    if m == 0 {
        return n  // только вставки
    }
    
    if n == 0 {
        let cursedSet = Set(cursed)
        for i in 0..<m {
            if cursedSet.contains(i) {
                return -1
            }
        }
        return m
    }
    
    
    let a = Array(s1)
    let b = Array(s2)
    
    let cursedSet = Set(cursed)
    let INF = Int.max / 2
    
    // Базовый случай: dp[0][j] = j (только вставки)
    var prev = Array(0...n)
    
    for i in 1...m {
        var cur = Array(repeating: 0, count: n + 1)
        
        // Базовый случай: dp[i][0] (удаление всех символов из A[0..i-1])
        let isCursed = cursedSet.contains(i - 1)
        let isZ = a[i-1] == "Z"
        let canDelete = !(isCursed && !isZ)
        
        if canDelete {
            cur[0] = prev[0] + 1
        } else {
            cur[0] = INF
        }
        
        for j in 1...n {
            let cost = a[i-1] == b[j-1] ? 0 : 1
            
            let del = isCursed ? INF : prev[j] + 1
            let ins = cur[j-1] + 1
            let rep = (isCursed && !isZ) ? INF : prev[j-1] + cost
            
            cur[j] = min(del, ins, rep)
        }
    
        prev = cur
    }
    
    return prev[n] >= INF ? -1 : prev[n]
}


func solve4_2() {
    
    // reading
    let s1 = readLine()!
    let s2 = readLine()!
    let cursed = readLine()!.split(separator: " ").map { Int($0)! }
    
    
    // alg
    let cnt = minErrorDistOpt(cursed, s1, s2)
    print(cnt)

}
