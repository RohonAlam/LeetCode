# Painter's Partition

Problem

There is fence which consists of  wooden blocks with each block having a number written on it represented by an array . The painter is also given two numbers  and  . He is given the task to paint the fence using at most  colors. But there are certain conditions which the painter must follow while painting:

- He has to paint the fence in sequential manner from left to right i.e, first paint the first block then second block and so on without leaving any block not being painted. 
- He will also use colors in sequential manner i.e, first paint with 1st color,then with 2nd color and so on. Note that he can paint any number of blocks sequentially with a single color and a color once used cannot be reused.
- The sum of numbers written on blocks painted with same color must lie between  and  ( both inclusive ).

    The painter wants to know in how many ways can he paint the fence.Since the answer can be large, find the answer modulo .

## **Input Format**

![[Pasted image 20260730114545.png]]

## **Output Format**

![[Pasted image 20260730114603.png]]

Time Limit: 10

Memory Limit: 256

Source Limit:

Explanation

The ways of painting are:

{(3),(5),(1,2),(6)} -> Painting 1st block with 1st color,2nd with 2nd, 3rd and 4th with 3rd and 4th block with 4th color.

{(3,5),(1,2),(6)}, {(3),(5),(1,2,6)}, {(3,5),(1,2,6)}, {(3),(5,1),(2,6)}, {(3,5,1),(2),(6)}, {(3,5,1),(2,6)}, {(3,5,1,2),(6)}