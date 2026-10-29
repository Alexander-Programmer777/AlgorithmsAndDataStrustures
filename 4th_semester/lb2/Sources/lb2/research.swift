import Foundation


struct ExperimentResult {
    let N: Int
    let run: Int
    let timeMs: Double
    let steps: Int
}

func generateRandomMatrix(n: Int, maxWeight: Int = 20) -> [[Double]] {
    var m = Array(repeating: Array(repeating: 0.0, count: n), count: n)
    for i in 0..<n {
        for j in 0..<n {
            if i == j {
                m[i][j] = -1
            } else {
                m[i][j] = Double(Int.random(in: 1...maxWeight))
            }
        }
    }
    return m
}

func runExperiment() {
    // 10 различных N:
    let sizes = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    let runsPerSize = 10

    var results: [ExperimentResult] = []

    print("Запуск эксперимента...")
    print("Размеры: \(sizes)")
    print("Всего запусков: \(sizes.count * runsPerSize)")

    for n in sizes {
        print("\n=== N = \(n) ===")

        for run in 0..<runsPerSize {
            let matrix = generateRandomMatrix(n: n)

            let start = Date()
            let solution = solveTSP(costMatrix: matrix)
            let timeMs = Date().timeIntervalSince(start) * 1000.0

            results.append(ExperimentResult(
                N: n,
                run: run,
                timeMs: timeMs,
                steps: solution.steps
            ))

            print(".", terminator: "")
            fflush(stdout)
        }
        print(" готово")
    }

    saveResultsToCSV(results: results)
    printStats(results: results)
}

func saveResultsToCSV(results: [ExperimentResult]) {
    let fileManager = FileManager.default
    let currentPath = fileManager.currentDirectoryPath
    let filename = "tsp_experiment_results.csv"
    let fullPath = (currentPath as NSString).appendingPathComponent(filename)

    print("Пытаемся сохранить в: \(fullPath)")

    var csvString = "N,run,timeMs,steps\n"
    for r in results {
        csvString += "\(r.N),\(r.run),\(r.timeMs),\(r.steps)\n"
    }

    do {
        try csvString.write(toFile: fullPath, atomically: true, encoding: .utf8)
        print("Файл успешно сохранен: \(fullPath)")
        if fileManager.fileExists(atPath: fullPath) {
            let attrs = try fileManager.attributesOfItem(atPath: fullPath)
            print("Файл существует, размер: \(attrs[.size] ?? 0) байт")
        }
    } catch {
        print("Ошибка при сохранении: \(error.localizedDescription)")
    }
}

// debug output function
func printStats(results: [ExperimentResult]) {
    var stats: [Int: (count: Int, timeSum: Double, stepsSum: Int)] = [:]

    for r in results {
        var s = stats[r.N] ?? (0, 0.0, 0)
        s.count += 1
        s.timeSum += r.timeMs
        s.stepsSum += r.steps
        stats[r.N] = s
    }

    print("\n=== Сводная статистика ===")
    print("N\tavgTimeMs\tavgSteps\tcount")

    for n in stats.keys.sorted() {
        if let s = stats[n] {
            let avgTime = s.timeSum / Double(s.count)
            let avgSteps = Double(s.stepsSum) / Double(s.count)
            print("\(n)\t\(String(format: "%.2f", avgTime))\t\(String(format: "%.1f", avgSteps))\t\(s.count)")
        }
    }
}

