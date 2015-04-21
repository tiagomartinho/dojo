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
    
    var score:Int {
        return rolls.reduce(0,combine: +)
    }
    
    func roll(pins:Int){
        rolls.append(pins)
    }
}