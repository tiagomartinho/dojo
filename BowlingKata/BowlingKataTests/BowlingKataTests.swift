//
//  BowlingKataTests.swift
//  BowlingKataTests
//
//  Created by Martinho on 20/04/15.
//  Copyright (c) 2015 Martinho. All rights reserved.
//

import UIKit
import XCTest

class BowlingKataTests: XCTestCase {
    
    var bowlingGame:BowlingGame?
    
    override func setUp() {
        super.setUp()
        bowlingGame = BowlingGame()
    }
    
    // MARK: Tests

    func testEmptyGame() {
        rollManyTimes(20,knockingPins:0)
        XCTAssertEqual(0,bowlingGame!.score)
    }
    
    func testAllOnesGame() {
        rollManyTimes(20,knockingPins:1)
        XCTAssertEqual(20,bowlingGame!.score)
    }
    
    func testOneSpare() {
        rollSpare()
        bowlingGame!.roll(3)
        rollManyTimes(17,knockingPins:0)
        XCTAssertEqual(16,bowlingGame!.score)
    }
    
    func testOneStrike() {
        rollStrike()
        bowlingGame!.roll(3)
        bowlingGame!.roll(4)
        rollManyTimes(16,knockingPins:0)
        XCTAssertEqual(24,bowlingGame!.score)
    }
    
    func testPerfectGame() {
        rollManyTimes(12,knockingPins:10)
        XCTAssertEqual(300,bowlingGame!.score)
    }
    
    // MARK: Roll utilities methods
    
    func rollManyTimes(n:Int,knockingPins:Int){
        for i in 1...n {
            bowlingGame!.roll(knockingPins)
        }
    }
    
    func rollSpare(){
        bowlingGame!.roll(5)
        bowlingGame!.roll(5)
    }
    
    func rollStrike(){
        bowlingGame!.roll(10)
    }
}
