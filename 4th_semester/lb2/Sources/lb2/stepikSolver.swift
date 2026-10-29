import Foundation

struct TSPSolution {
    let path: [Int]
    let cost: Double
    let steps: Int
}

// solver for tests and research
func solveTSP(costMatrix: [[Double]]) -> TSPSolution {
    let n = costMatrix.count
    var bestCost = Double.infinity
    var bestPath: [Int] = []

    var steps = 0

    var initialPath = [0]
    var visited = [Bool](repeating: false, count: n)
    visited[0] = true

    func lowerBound(path: [Int], visited: [Bool]) -> Double { // оценка (лучший случай) минимальной стоимости любого полного маршрута, который начинается с уже пройденного пути path
        steps += 1

        let currentCity = path.last!
        var bound = 0.0

        for i in 0..<path.count - 1 { // Стоимость уже пройденного пути
            bound += costMatrix[path[i]][path[i + 1]]
        }

        var minToUnvisited = Double.infinity
        for j in 0..<n { // Минимальный выход из последнего города в любой непосещённый
            if !visited[j] && costMatrix[currentCity][j] != -1 {
                minToUnvisited = min(minToUnvisited, costMatrix[currentCity][j])
            }
        }
        if minToUnvisited == Double.infinity {
            return Double.infinity
        }
        bound += minToUnvisited

        
        // проход по непосещенным городам и считаем
        for i in 0..<n {
            if !visited[i] && i != currentCity {
                var minOut = Double.infinity // Минимальное выходящее ребро
                for j in 0..<n {
                    if j != i && costMatrix[i][j] != -1 {
                        if !visited[j] || j == 0 {
                            minOut = min(minOut, costMatrix[i][j])
                        }
                    }
                }

                var minIn = Double.infinity // Минимальное входящее ребро
                for j in 0..<n {
                    if j != i && costMatrix[j][i] != -1 {
                        if !visited[j] || j == currentCity {
                            minIn = min(minIn, costMatrix[j][i])
                        }
                    }
                }
                // добавлем их
                if minOut != Double.infinity {
                    bound += minOut
                }
                if minIn != Double.infinity {
                    bound += minIn
                }
            }
        }

        return bound / 2.0 // тк учтено дважды
    } // PS оценка приблизительная и не всегда допустимая, но тем не менее хорошо помогает откидывать неоптимальные пути во время перебора
    

    func branchAndBound(path: inout [Int], visited: inout [Bool], currentCost: Double) {
        steps += 1

        if path.count == n { // полный путь
            if costMatrix[path.last!][0] != -1 {
                let totalCost = currentCost + costMatrix[path.last!][0]
                if totalCost < bestCost {
                    bestCost = totalCost
                    bestPath = path
                }
            }
            return
        }

        let lb = lowerBound(path: path, visited: visited)
        if lb >= bestCost {
            return // отсечение
        }

        let currentCity = path.last!
        for nextCity in 0..<n {
            if !visited[nextCity] && costMatrix[currentCity][nextCity] != -1 {
                let newCost = currentCost + costMatrix[currentCity][nextCity]
                if newCost < bestCost {
                    
                    visited[nextCity] = true
                    path.append(nextCity)
                    
                    branchAndBound(path: &path, visited: &visited, currentCost: newCost)
                    
                    path.removeLast() // backtracking
                    visited[nextCity] = false
                }
            }
        }
    }

    branchAndBound(path: &initialPath, visited: &visited, currentCost: 0)

    return TSPSolution(path: bestPath, cost: bestCost, steps: steps)
}


// solver for stepik task
func solve() {
    let n = Int(readLine()?.trimmingCharacters(in: .whitespacesAndNewlines) ?? "") ?? 0
    var costMatrix: [[Double]] = []

    for _ in 0..<n {
        if let line = readLine() {
            let row = line.trimmingCharacters(in: .whitespacesAndNewlines)
                .split(separator: " ")
                .compactMap { Double($0) }
            costMatrix.append(row)
        }
    }

    let result = solveTSP(costMatrix: costMatrix)
    // let fullPath = result.path + [0]

    print(result.path.map { String($0) }.joined(separator: " "))
    print(String(format: "%.1f", result.cost))
}

