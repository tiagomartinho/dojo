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
    private var scoreTotal = 0
    
    func roll(pins:Int){
        scoreTotal += pins
    }
    
    func score()->Int{
        return scoreTotal
    }
}