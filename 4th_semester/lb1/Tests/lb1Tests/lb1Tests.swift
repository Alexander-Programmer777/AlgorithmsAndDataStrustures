import Testing
@testable import lb1

// Тестируем программу для варианта 5 согласно ТЗ
struct SolverWithRequiredTests {

    // 1. Пустой список обязательных квадратов (не должно быть ошибок)
    @Test
    func testEmptyRequired() throws {
        let (count, squares) = try solveWithRequired(N: 5, required: [])
        #expect(count == squares.count)
        #expect(count > 0)
    }

    // 2. Один обязательный квадрат
    @Test
    func testSingleRequired() throws {
        let (_, squares) = try solveWithRequired(N: 6, required: [3])
        #expect(squares.contains { $0.w == 3 })
    }

    // 3. Несколько обязательных квадратов
    @Test
    func testMultipleRequired() throws {
        let (_, squares) = try solveWithRequired(N: 8, required: [3, 2])
        #expect(squares.contains { $0.w == 3 })
        #expect(squares.contains { $0.w == 2 })
    }

    // 4. Ошибка (невозможность решить): обязательный квадрат слишком большой
    @Test
    func testRequiredTooLarge() {
        #expect(throws: SolveError.impossible) {
            _ = try solveWithRequired(N: 5, required: [5])
        }
    }

    // 5. Ошибка: обязательных квадратов слишком много по площади
    // 4*4 = 16, 3^2 + 3^2 + 3^2 = 27 > 16
    @Test
    func testRequiredTooMany() {
        #expect(throws: SolveError.impossible) {
            _ = try solveWithRequired(N: 4, required: [3, 3, 3])
        }
    }

    // 6. Проверка, что решение действительно покрывает всю площадь
    @Test
    func testFullCoverage() throws {
        let (_, squares) = try solveWithRequired(N: 6, required: [])
        var covered = 0
        for s in squares { covered += s.w * s.w }
        #expect(covered == 36)
    }

    // 7. Проверка, что обязательные квадраты точно используются
    @Test
    func testRequiredExactUsage() throws {
        let req = [2, 2, 3]
        let (_, squares) = try solveWithRequired(N: 7, required: req)

        let used = squares.map { $0.w }
        for w in req {
            #expect(used.filter { $0 == w }.count >= 1)
        }
    }
    
    // 8. Кастомный тест
    @Test
    func testRandomRequired() throws {
         let (count, squares) = try solveWithRequired(N: 4, required: [2, 2, 2, 2])
        #expect(count == 4)
        
        for square in squares {
            #expect(square.w == 2)
        }
    }

    // 9. Проверка генератора списков (без дубликатов)
    @Test
    func testGeneratorNoDuplicates() {
        let list = generateSquareList(maxSize: 5, allowDuplicates: false, length: 6)
        #expect(list.count == 5)
    }

    // 10. Проверка генератора списков (с дубликатами)
    @Test
    func testGeneratorWithDuplicates() {
        let list = generateSquareList(maxSize: 3, allowDuplicates: true, length: 10)
        #expect(list.count == 10)
    }
}
