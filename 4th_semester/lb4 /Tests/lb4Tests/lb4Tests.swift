//import Testing
//@testable import lb4
//
//
//struct KMPTests {
//
//    // MARK: - Базовые тесты
//    @Test
//    func testExample() throws {
//        let res = KMP("ab", "abab")
//        #expect(res == [0, 2])
//    }
//
//    @Test
//    func testSingleMatch() throws {
//        let res = KMP("abc", "xxabcxx")
//        #expect(res == [2])
//    }
//
//    @Test
//    func testMultipleMatches() throws {
//        let res = KMP("aba", "ababaaba")
//        #expect(res == [0, 2, 5])
//    }
//
//    @Test
//    func testNoMatches() throws {
//        let res = KMP("abc", "defgh")
//        #expect(res == [-1])
//    }
//
//    @Test
//    func testPatternLongerThanText() throws {
//        let res = KMP("abcdef", "abc")
//        #expect(res == [-1])
//    }
//
//    // MARK: - Краевые случаи
//
//    @Test
//    func testEmptyPattern() throws {
//        let res = KMP("", "abc")
//        #expect(res == [-1])
//    }
//
//    @Test
//    func testEmptyText() throws {
//        let res = KMP("abc", "")
//        #expect(res == [-1])
//    }
//
//    @Test
//    func testBothEmpty() throws {
//        let res = KMP("", "")
//        #expect(res == [-1])
//    }
//
//    @Test
//    func testFullMatch() throws {
//        let res = KMP("hello", "hello")
//        #expect(res == [0])
//    }
//
//    @Test
//    func testOverlappingMatches() throws {
//        let res = KMP("aaa", "aaaaa")
//        #expect(res == [0, 1, 2])
//    }
//}
//
//
//struct KMPCycleShiftTests {
//
//    // MARK: - Базовые тесты
//    @Test
//    func testExample() throws {
//        let res = KMPCycleShift("abcdef", "defabcdefabc")
//        #expect(res == 3)
//    }
//
//    @Test
//    func testSimpleShift() throws {
//        let res = KMPCycleShift("bca", "abcabc")
//        #expect(res == 1)
//    }
//
//    @Test
//    func testNoShiftPossible() throws {
//        let res = KMPCycleShift("abc", "abdabd")
//        #expect(res == -1)
//    }
//
//    @Test
//    func testIdenticalStrings() throws {
//        let res = KMPCycleShift("abc", "abcabc")
//        #expect(res == 0)
//    }
//
//    // MARK: - Краевые случаи
//
//    @Test
//    func testLengthConditionViolation() throws {
//        let res = KMPCycleShift("abcde", "wwwqqqrrrrcdeabc")
//        #expect(res == -1)
//    }
//
//    @Test
//    func testSingleCharacter() throws {
//        let res = KMPCycleShift("a", "aa")
//        #expect(res == 0)
//    }
//
//    @Test
//    func testAllSameCharacters() throws {
//        let res = KMPCycleShift("aaa", "aaaaaa")
//        #expect(res == 0)
//    }
//
//}
//
