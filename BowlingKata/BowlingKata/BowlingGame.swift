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
    
    func roll(pins:Int){
        rolls.append(pins)
    }
    
    func score()->Int{
        var score = 0
        for pins in rolls {
            score+=pins
        }
        return score
    }
}