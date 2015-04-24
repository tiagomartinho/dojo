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
    
    func testEmptyGame() {
        rollManyTimes(20,knockingPins:0)
        XCTAssertEqual(0,bowlingGame!.score)
    }
    
    func testAllOnesGame() {
        rollManyTimes(20,knockingPins:1)
        XCTAssertEqual(20,bowlingGame!.score)
    }
    
    func rollManyTimes(n:Int,knockingPins:Int){
        for i in 1...n {
            bowlingGame!.roll(knockingPins)
        }
    }
    
    func testOneSpare() {
        rollSpare()
        bowlingGame!.roll(3)
        rollManyTimes(17,knockingPins:0)
        XCTAssertEqual(16,bowlingGame!.score)
    }
    
    func rollSpare(){
        bowlingGame!.roll(5)
        bowlingGame!.roll(5)
    }
}
