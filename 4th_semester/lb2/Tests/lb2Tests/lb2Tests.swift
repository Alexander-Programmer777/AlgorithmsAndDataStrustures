import Testing
@testable import lb2

struct TSPSolverTests {

    // 1. Пример 1 из задания
    @Test
    func testSample1() throws {
        let matrix: [[Double]] = [
            [-1, 1, 3],
            [3, -1, 1],
            [1, 2, -1]
        ]

        let result = solveTSP(costMatrix: matrix)

        #expect(result.cost == 3.0)
        #expect(result.path.count == 3)
        #expect(result.path.first == 0)
        #expect(Set(result.path) == Set([0, 1, 2]))
    }

    // 2. Пример 2 из задания
    @Test
    func testSample2() throws {
        let matrix: [[Double]] = [
            [-1, 3, 4, 1],
            [1, -1, 3, 4],
            [9, 2, -1, 4],
            [8, 9, 2, -1]
        ]

        let result = solveTSP(costMatrix: matrix)

        #expect(result.cost == 6.0)
        #expect(result.path.count == 4)
        #expect(result.path.first == 0)
        #expect(Set(result.path) == Set([0, 1, 2, 3]))
    }

    // 3. Симметричная матрица 4x4
    @Test
    func testSymmetric4() throws {
        let matrix: [[Double]] = [
            [-1, 2, 3, 4],
            [2, -1, 5, 6],
            [3, 5, -1, 1],
            [4, 6, 1, -1]
        ]

        let result = solveTSP(costMatrix: matrix)

        #expect(result.path.count == 4)
        #expect(result.path.first == 0)
        #expect(Set(result.path) == Set([0, 1, 2, 3]))
        #expect(result.cost < Double.infinity)
    }

    // 4. Минимальный случай N = 2
    @Test
    func testN2() throws {
        let matrix: [[Double]] = [
            [-1, 5],
            [5, -1]
        ]

        let result = solveTSP(costMatrix: matrix)

        #expect(result.path.count == 2)
        #expect(result.path.first == 0)
        #expect(Set(result.path) == Set([0, 1]))
        #expect(result.cost == 10.0)
    }

    // 5. Проверка, что шагов > 0 и решение конечное
    @Test
    func testStepsPositive() throws {
        let matrix: [[Double]] = [
            [-1, 2, 9],
            [1, -1, 6],
            [15, 7, -1]
        ]

        let result = solveTSP(costMatrix: matrix)

        #expect(result.steps > 0)
        #expect(result.cost < Double.infinity)
    }
}
