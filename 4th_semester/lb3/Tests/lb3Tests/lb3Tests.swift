import Testing
@testable import lb3

struct EditDistanceTests {
    
    // MARK: - Базовые тесты (без проклятых)
    
    // 1. Тест из задания (entrance -> reenterable)
    @Test
    func testSampleFromTask() throws {
        let cursed: [Int] = []
        let (path, cost) = minErrorDist(cursed, "entrance", "reenterable", 1, 1, 1)
        
        #expect(cost == 5)
        #expect(path.count == 11) // длина пути для этих строк
    }
    
    // 2. Одинаковые строки
    @Test
    func testIdenticalStrings() throws {
        let cursed: [Int] = []
        let (path, cost) = minErrorDist(cursed, "hello", "hello", 1, 1, 1)
        
        #expect(cost == 0)
        #expect(path == "MMMMM")
    }
    
    // 3. Пустая строка A
    @Test
    func testEmptyA() throws {
        let cursed: [Int] = []
        let (path, cost) = minErrorDist(cursed, "", "abc", 2, 3, 4)
        
        #expect(cost == 3 * 3) // 3 вставки по 3 = 9
        #expect(path == "III")
    }
    
    // 4. Пустая строка B
    @Test
    func testEmptyB() throws {
        let cursed: [Int] = []
        let (path, cost) = minErrorDist(cursed, "abc", "", 2, 3, 4)
        
        #expect(cost == 3 * 4) // 3 удаления по 4 = 12
        #expect(path == "DDD")
    }
    
    // 5. Разные стоимости
    @Test
    func testDifferentCosts() throws {
        let cursed: [Int] = []
        let (_, cost) = minErrorDist(cursed, "ab", "ba", 10, 1, 1)
        
        // Дешевле вставить 'b' и удалить 'a' (1+1=2), чем заменять (10)
        #expect(cost == 2)
    }
    
    // MARK: - Тесты с проклятыми элементами
    
    // 6. Проклятый символ (не Z) — нельзя удалять и заменять
    @Test
    func testCursedNotZ() throws {
        let cursed = [0] // символ 'a' проклят
        let (_, cost) = minErrorDist(cursed, "ab", "bb", 1, 1, 1)
        
        // 'a' нельзя удалить или заменить -> преобразование невозможно
        #expect(cost == -1)
    }
    
    // 7. Проклятый символ Z — можно заменять, нельзя удалять
    @Test
    func testCursedZ() throws {
        let cursed = [0] // 'Z' проклят
        let (_, cost) = minErrorDist(cursed, "Zb", "Xb", 1, 1, 1)
        
        // Можно заменить Z на X (стоимость 1)
        #expect(cost == 1)
    }
    
    // 8. Проклятый Z нельзя удалить
    @Test
    func testCursedZCannotDelete() throws {
        let cursed = [0] // 'Z' проклят
        let (_, cost) = minErrorDist(cursed, "Z", "", 1, 1, 1)
        
        #expect(cost == -1) // нельзя удалить Z
    }
    

}


struct EditDistanceOptTests {
    
    // MARK: Общие тесты (без проклятых)
    
    // 1. Базовый тест (entrance -> reenterable)
    @Test
    func testSampleFromTask() throws {
        let cursed: [Int] = []
        let cost = minErrorDistOpt(cursed, "entrance", "reenterable")
        
        #expect(cost == 5)
    }
    
    // 2. Одинаковые строки
    @Test
    func testIdenticalStrings() throws {
        let cursed: [Int] = []
        let cost = minErrorDistOpt(cursed, "hello", "hello")
        
        #expect(cost == 0)
    }
    
    // 3. Пустая строка A
    @Test
    func testEmptyA() throws {
        let cursed: [Int] = []
        let cost = minErrorDistOpt(cursed, "", "abc")
        
        #expect(cost == 3) // 3 вставки по 1
    }
    
    // 4. Пустая строка B
    @Test
    func testEmptyB() throws {
        let cursed: [Int] = []
        let cost = minErrorDistOpt(cursed, "abc", "")
        
        #expect(cost == 3) // 3 удаления по 1
    }
    
    // 5. Строки разной длины
    @Test
    func testDifferentLength() throws {
        let cursed: [Int] = []
        let cost = minErrorDistOpt(cursed, "cat", "cats")
        
        #expect(cost == 1) // одна вставка 's'
    }
    
    // 6. Полная замена всех символов
    @Test
    func testFullReplace() throws {
        let cursed: [Int] = []
        let cost = minErrorDistOpt(cursed, "abc", "xyz")
        
        #expect(cost == 3) // 3 замены
    }
    
    
    // MARK: Проклятые эл-ты
    
    // 7. Проклятый символ (не Z) — невозможно
    @Test
    func testCursedNotZ() throws {
        let cursed = [0]
        let cost = minErrorDistOpt(cursed, "ab", "bb")
        
        #expect(cost == -1)
    }
    
    // 8. Проклятый Z — можно заменять
    @Test
    func testCursedZ() throws {
        let cursed = [0]
        let cost = minErrorDistOpt(cursed, "Zb", "Xb")
        
        #expect(cost == 1)
    }
    
    // 9. Проклятый Z нельзя удалить
    @Test
    func testCursedZCannotDelete() throws {
        let cursed = [0]
        let cost = minErrorDistOpt(cursed, "Z", "")
        
        #expect(cost == -1)
    }
    
    // 10. Проклятый Z + обычный символ
    @Test
    func testMixedCursed() throws {
        let cursed = [1] // 'Z' проклят
        let cost = minErrorDistOpt(cursed, "aZ", "bX")
        
        #expect(cost == 2) // замена a->b (1) + замена Z->X (1)
    }
}
