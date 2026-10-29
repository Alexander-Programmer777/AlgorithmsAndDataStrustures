func computePrefixFunctions(_ s: String) -> [Int] {
    
    let n = s.count
    let pattern = Array(s.utf8)
    var p = [Int](repeating: 0, count: n)
    
    for i in 1..<n {
        var k = p[i-1]
        
        while k > 0 && pattern[i] != pattern[k] {
            k = p[k-1]
        }
        
        if pattern[i] == pattern[k] {
            k += 1
        }
        
        p[i] = k
    }
    
    return p
}


func KMP(_ p: String, _ t: String) -> [Int] {
    if p.isEmpty || t.isEmpty { // edge case: empty string
        return [-1]
    }
    
    let tArray = Array(t.utf8) // memory opt
    let pArray = Array(p.utf8)
    
    let n = t.count
    let m = p.count
    let prefixes = computePrefixFunctions(p) // prefixes for pattern string (p)
    var res: [Int] = []
    
    var j = 0 // j - pattern pointer
    for i in 0..<n { // i - text pointer
        
        while j > 0 && tArray[i] != pArray[j] {
            j = prefixes[j - 1] // откат не в j = 0, как в наивном алгоритме, а по префикс функции
        }
        
        if tArray[i] == pArray[j] {
            j += 1
        }
        
        if j == m {
            res.append(i - m + 1)
            j = prefixes[j - 1]
        }
    }
    
    return res.isEmpty ? [-1] : res
}


func solveKMP() -> [Int] {
    
    // Чтение входных данных
    let s1 = readLine()!
    let s2 = readLine()!
    
    
    // Алгоритм
    let ans = KMP(s1, s2)
    
    return ans
}
