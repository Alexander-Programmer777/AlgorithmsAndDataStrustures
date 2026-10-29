func KMPCycleShift(_ p: String, _ t: String) -> Int {
    if p.isEmpty || t.isEmpty { // edge case: empty string
        return -1
    }
    
    let tArray = Array(t.utf8)
    let pArray = Array(p.utf8)
    
    let n = t.count
    let m = p.count
    
    // условие, что строки одинаковой длины, но в t мы подаем уже удвоенную строку
    if n != 2*m {
        return -1
    }
    
    let prefixes = computePrefixFunctions(p) // prefixes for pattern string (p)
    
    var j = 0
    for i in 0..<n { // text loop
        
        while j > 0 && tArray[i] != pArray[j] {
            j = prefixes[j - 1]
        }
        
        if tArray[i] == pArray[j] {
            j += 1
        }
        
        if j == m {
            return i - m + 1 // первый найденный из предыдущего алгоритма = ответ
        }
    }
    
    return -1
}


func solveKMPCycleShift() -> Int {
    
    // Чтение входных данных
    let s1 = readLine()!
    let s2 = readLine()!
    
//    if s1.count != s2.count { // вынесено в KMPCycleShift для тестирования крайнего случая
//        return -1
//    }
    
    
    // Алгоритм
    let ans = KMPCycleShift(s2, s1 + s1)
    
    return ans
}
