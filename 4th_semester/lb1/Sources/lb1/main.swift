import Foundation


// For stepik
//guard let N = Int(readLine()!), N >= 2 else {
//    print("Ошибка: N должно быть не менее 2")
//    exit(1)
//}
//
//let startTime = Date()
//let result = solve(N)
//let endTime = Date()
//let timeInterval = endTime.timeIntervalSince(startTime)
//
//print(result.0)
//for el in result.1 {
//    print(el[0], el[1], el[2])
//}
//
//print("Total time is \(timeInterval) seconds")


// total stepik check
func totalMeasurement() {
    for N in 2...40 {
        let startTime = Date()
        _ = solve(N)
        let endTime = Date()
        let timeInterval = endTime.timeIntervalSince(startTime)
        print("N = \(N), Total time is \(timeInterval) seconds")
    }
}

//totalMeasurement()



// experiment for option 5.5
runExperiment()


