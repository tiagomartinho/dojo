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
    private var rolls = [Int](count: 21, repeatedValue: 0)
    
    private let frames = 10

    private var currentRoll = 0
    
    var score:Int {
        var score = 0
        var frameIndex = 0
        for _ in 1...frames {
            if rolls[frameIndex] == 10 {
                score += 10 + rolls[frameIndex+1] + rolls[frameIndex+2]
            }
            else { if isSpare(frameIndex) {
                score += 10 + rolls[frameIndex+2]
                frameIndex++
            }
            else{
                score += rolls[frameIndex] + rolls[frameIndex+1]
                frameIndex++
                }
            }
            frameIndex++
        }
        return score
    }
    
    func roll(pins:Int){
        rolls[currentRoll++]=pins
    }
    
    func isSpare(frameIndex:Int)->Bool{
        return rolls[frameIndex] + rolls[frameIndex+1] == 10
    }
}