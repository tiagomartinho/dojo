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
    
    var bowlingGame = BowlingGame()
    
    override func setUp() {
        super.setUp()
    }
    
    override func tearDown() {
        super.tearDown()
    }
    
    func testEmptyGame() {
        for i in 1...20 {
            bowlingGame.roll(0)
        }
        XCTAssertEqual(0,bowlingGame.score())
    }
    
}
