# Circular-motion-and-sinusoid-motion
How it works with sin and cos, circular motion and sinusoid motion.
> A sine wave is a plane curve defined in rectangular coordinates by the equation.
---
1. In order to realize movement around a circle, we must first find out the distance around which the object will move;
 <self.__radius = radius> 
2. Do not forget about the mathematical module;
 <from math import cos, sin, pi>
3. Create a variable angle and then increase it and convert it to radians;
 <self.__angle = 0>
 <self.__angle += round(1/self.__speed, 2)>
 <self.__radian = self.__angle * pi/180>
4. If the angle is greater than or equal to 360, then we reset it, this is necessary for the correct calculation of the angle, and in order for the "integer" to overflow;
 <if self.__angle >= 360: self.__angle = 0>
5. The last one is we take the position around it to rotate and fold it.
 <self.pos = pos>
 <self.rect.centerx = (self.__radius*cos(self.__radian*direction)) + self.pos[0]>
 <self.rect.centery = (self.__radius*sin(self.__radian*direction)) + self.pos[1]>
---
I hope I interpreted my code clearly, drawing graphics, I think you will understand the creation of the object too...
My youtube channel and videos: [Michael S](https://youtu.be/3syDcuS7giI)
