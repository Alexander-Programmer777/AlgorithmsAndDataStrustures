import Foundation

// Структура для хранения результатов
struct ExperimentResult {
    let length: Int
    let allowDuplicates: Bool
    let success: Bool
    let timeMs: Double
    let N: Int
}

func runExperiment() {
    let maxSize = 9 // в 1 эксперименте был 10, во втором 5, в 3 - 9
    let listLengths = [2, 4, 6, 8, 10, 12]
    let runsPerLength = 10
    
    let N = 11   // размер доски, в 1 эксперименте был 9, во 2 и 3 - 11
    
    var results: [ExperimentResult] = []
    
    print("Запуск эксперимента...")
    print("N = \(N), maxSize = \(maxSize)")
    print("Всего запусков: \(2 * listLengths.count * runsPerLength) = \(2 * 6 * 10)")
    
    for allowDuplicates in [true, false] {
        let dupType = allowDuplicates ? "с дубликатами" : "без дубликатов"
        print("\n=== \(dupType) ===")
        
        for length in listLengths {
            print("  Длина \(length): ", terminator: "")
            
            for _ in 0..<runsPerLength {
                // Генерация списка
                let required = generateSquareList(
                    maxSize: maxSize,
                    allowDuplicates: allowDuplicates,
                    length: length
                )
                
                // Замер времени
                let start = Date()
                var success = false
                
                do {
                    _ = try solveWithRequired(N: N, required: required)
                    success = true
                } catch {
                    success = false
                }
                
                let timeMs = Date().timeIntervalSince(start) * 1000.0
                
                results.append(ExperimentResult(
                    length: length,
                    allowDuplicates: allowDuplicates,
                    success: success,
                    timeMs: timeMs,
                    N: N
                ))
                
                print(".", terminator: "")
                fflush(stdout)
            }
            print(" готово")
        }
    }
    
    saveResultsToCSV(results: results)
    printStats(results: results)
}

func saveResultsToCSV(results: [ExperimentResult]) {
    // Получаем путь к рабочей директории
    let fileManager = FileManager.default
    let currentPath = fileManager.currentDirectoryPath
    let filename = "experiment_results.csv"
    let fullPath = (currentPath as NSString).appendingPathComponent(filename)
    
    print("Пытаемся сохранить в: \(fullPath)")
    
    var csvString = "length,allowDuplicates,success,timeMs,N\n"
    
    for r in results {
        csvString += "\(r.length),\(r.allowDuplicates ? 1 : 0),\(r.success ? 1 : 0),\(r.timeMs),\(r.N)\n"
    }
    
    do {
        try csvString.write(toFile: fullPath, atomically: true, encoding: .utf8)
        print("Файл успешно сохранен: \(fullPath)")
        
        // Проверяем, что файл действительно создан
        if fileManager.fileExists(atPath: fullPath) {
            print("Файл существует, размер: \(try fileManager.attributesOfItem(atPath: fullPath)[.size] ?? 0) байт")
        }
    } catch {
        print("Ошибка при сохранении: \(error.localizedDescription)")
    }
}



func printStats(results: [ExperimentResult]) {
    // Группируем по длине и типу
    var stats: [String: (total: Int, success: Int, timeSum: Double)] = [:]
    
    for r in results {
        let key = "\(r.length)_\(r.allowDuplicates ? 1 : 0)"
        var stat = stats[key] ?? (0, 0, 0)
        stat.total += 1
        if r.success {
            stat.success += 1
            stat.timeSum += r.timeMs
        }
        stats[key] = stat
    }
    
    // debug output
    print("\n=== Сводная статистика ===")
    print("Длина\tТип\tУспех(%)\tСр.время(мс)\tВсего")
    
    for length in [2, 4, 6, 8, 10, 12] {
        for dup in [true, false] {
            let key = "\(length)_\(dup ? 1 : 0)"
            if let stat = stats[key] {
                let successRate = Double(stat.success) / Double(stat.total) * 100
                let avgTime = stat.success > 0 ? stat.timeSum / Double(stat.success) : 0
                print("\(length)\t\(dup ? "с дубликатами " : "без дубликатов")\t\(String(format: "%.1f", successRate))%\t\(String(format: "%.2f", avgTime))\t\(stat.total)")
            }
        }
    }
}


