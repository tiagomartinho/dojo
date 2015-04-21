//
//  BowlingGame.swift
//  BowlingKata
//
//  Created by Martinho on 20/04/15.
//  Copyright (c) 2015 Martinho. All rights reserved.
//

import Foundation

class BowlingGame
{
    private var rolls = [Int]()
    
    private let frames = 10

    var score:Int {
        var score = 0
        var i = 0
        for _ in 1...frames {
            score += rolls[i] + rolls[i+1]
            i += 2
        }
        return score
    }
    
    func roll(pins:Int){
        rolls.append(pins)
    }
}