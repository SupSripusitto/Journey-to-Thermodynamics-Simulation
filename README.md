## Introduction | ภูมิหลัง

This project is my (own) first project on molecular simulation. I've not studied about molecular dynamics or simulation before, but I learn by my self with some foundations from high school concepts of gas kinetics and chemical engineering thermodynamics. I hope this could help everyone who seen this to be able to make your own simulation from scratch like I do now.  
  
---
โปรเจกนี้เป็นงาน (ส่วนตัว) ของผมเกี่ยวกับการจำลองโมเลกุลนะครับ ผมเป็นคนที่ไม่เคยมีโอกาสเรียนรู้เกี่ยวกับ molecular dynamics หรือการเขียนโปรแกรมจำลองต่าง ๆ มาก่อนเลยครับ แต่ผมเรียนรู้ทุกอย่างทั้งหมดนี้ด้วยตนเองโดยใช้แค่พื้นฐานความรู้ทฤษฎีจลน์แก๊สตอนม.ปลาย และวิชา thermodynamics ที่เรียนมาตอนปี 2 เท่านั้นครับ (ไม่จำเป็นต้องรู้มาก่อนก็ได้) ผมหวังว่าทุกคนจะได้เรียนรู้จนสามารถเอาไปต่อยอดสร้างการจำลองเหมือนที่ผมทำเพื่อใช้เปลี่ยนประเทศชาติและโลกใบนี้ให้ดีขึ้นไปด้วยกันได้นะครับ  
  
--- 
>**Let's learn together until we break our limit**  
>**มาเรียนรู้กันจนกว่าจะทลายขีดจำกัดของพวกเรากันครับ**  
>  
>_Supphawit Sripusitto (ศุภวิชญ์ ศรีภูสิตโต)_

## Ideal Gas Model | แบบจำลองแก๊สอุดมคติ

Ideal gas is the simplest model in thermodynamics to relate all states and properties (e.g., Temperature, Pressure, Density, Internal energy). Therefore, I think it's the most convinient way to start programming with the ideal gas model. As its name, ideal gas is not real gas, so there's some assumption to be consider. However, I choose only the core idea assumptions as below (no minor assumption).
- Gas molecules has no volume (volume is the volume of the container).
- No interaction between each molecule

The first assumption could be interpreted as there's no intermolecular collision i.e. each molecules collides only the container walls. Also, the second could be interpreted as all collisions are elastic (not losing kinetic energy).  
  
---
แก๊สอุดมคติคือแบบจำลองที่ง่ายที่สุดใน thermodynamics ที่สามารถเชื่อมโยงระหว่างสภาวะและสมบัติต่าง ๆ เช่น อุณหภูมิ ความดัน ความหนาแน่น พลังงานภายใน ได้แล้ว ดังนั้นผมคิดว่าเราควรเริ่มจากทางที่สบายที่สุดในการเริ่มเขียนโปรแกรมด้วยแค่หลักการของแก๊สอุดมคติ และก็เป็นไปตามชื่อแก๊สอุดมคติ (อุดมคติคือมีแค่ในจินตนาการ) มันไม่ใช่แก๊สจริง ๆ ดังนั้นมันจึงมีสมมติฐานบางอย่างให้เราต้องพิจารณา ในที่นี้ผมยกมาเพียงตัวหลัก ๆ เท่านั้น (เพราะมันมีเยอะจนจะจำกันไม่ไหว) เงื่อนไขต่าง ๆ ก็เป็นไปตามรายชื่อด้านล่างเลยครับ
- โมเลกุลแก๊สไม่มีปริมาตร (ปริมาตรแก๊สที่ใช้คือปริมาตรของภาชนะบรรจุแก๊สเท่านั้น)
- ไม่มีอันตรกิริยากันระหว่างโมเลกุล (ไม่ดูด ผลัก เฉือนกันด้วยแรงทางไฟฟ้าหรือแรงระหว่างโมเลกุลอื่น ๆ)

สมมติฐานตัวแรกตีความต่อมาได้ว่าไม่มีทางที่โมเลกุลจะชนกัน (จริง ๆ มันชนกันได้ แต่โอกาสจะคำนวณได้เป็น 0 เพราะมันต้องบังอิญอยู่ในแนวเส้นตรงที่ตัดกันพอดีเป๊ะจากพื้นที่เป็นอนันต์) นั่นคือจะมีการชนเพียงแค่ผนังของภาชนะเท่านั้น ส่วนอีกสมมติฐานตีความได้ว่าการชนผนังทุกครั้งเป็นการชนแบบยืดหยุ่น นั่นคือไม่เสียพลังงานจลน์สุทธิหลังกาารชน (เพราะมันไม่มีแรงภายนอกมากระทำ)

Additionally, velocity distribution is Maxwell-Boltzmann distribution. That is each velocity components have the Gaussian distrubution. We also known that average velocity should be 0; therefore, each velocity components have the same mean of 0. I make an assumption by which each velocity components are i.i.d (independent & identically distributed). Hence, each components should have the same root mean square value. That is root mean square of each components is $v_{rms}/\sqrt{2}$ (or $v_{rms}/\sqrt{3}$ for 3D). After analyzing, I found that variance of the distribution is the same as $v_{rms}$ of each components. So now, I can program the first simulation with accurate velocity distribution.

นอกจากนี้การกระจายตัวของความเร็วเป็นแบบ Maxwell-Boltzmann นั่นคือองค์ประกอบในแต่ละแกน (X,Y,Z) ของความเร็วมีการกระจายตัวแบบปกติ (Normal หรือ Gaussian distribution) และเรารู้อีกว่าความเร็วเฉลี่ยของแต่ละอนุภาคควรเป็น 0 ดังนั้นค่าเฉลี่ยของความเร็วในแต่ละแกนก็ต้องเป็น 0 ด้วย ตรงนี้ผมตั้งสมมติฐานว่าความเร็วในแต่ละแกนเป็น i.i.d. (เป็นอิสระจากกัน และมีการกระจายตัวแบบเดียวกัน) สรุปผลได้ว่าความเร็วในแต่ละแกนควรมีค่า rms (root mean square) เท่ากันทั้งหมด จะได้ว่าค่า rms ของแต่ละแกนคือ $v_{rms}/\sqrt{2}$ (หรือ $v_{rms}/\sqrt{3}$ สำหรับ 3 มิติ) หลังจากที่ผมลองวิเคราะห์ ผมพบว่าความแปรปรวนของการกระจายตัวมีค่าเดียวกับ $v_{rms}$ ของแต่ละแกน (ก็คือตัวที่เขียนก่อนหน้านั่นแหละ) ดังนั้นตอนนี้เราสามารถเขียน simulation ตัวแรกด้วยความเร็วที่กระจายตัวอย่างถูกต้องได้แล้วครับ

## Bouncing boundary conditions | ขอบเขตเด้งได้

As you can imagine, when particle hits the wall. It should bounce and not penetrate. Therefore, we need to analyze how particle trajectories are calculated. First, we use the second assumption of ideal gas. It could be interpreted as wall collisions are elastic i.e. no loss of kinetic energy. Hence, the particles momentum are conserved or the velocity just change direction to opposite side in an axis where particle collides. To implement, we need to check whether particle will get out of boundary or not. Then, we use the formula we analyzed which is $x_{k+1,actual} = 2x_{bound}-x_{k+1}$ to calculate the actual position of the collide particles. Last, we set velocity component where the particles collide to be negative of itself.

คงนึกออกใช่ไหมครับว่าถ้าอนุภาคชนกำแพงมันก็ควรเด้งกลับ ไม่ใช่ทะลุกำแพงไปเลย (ไม่อย่างนั้นเราจะมีกำแพงทำไม) ดังนั้นเราจำต้องวิเคราะห์ว่าวิถีการเคลื่อนที่ของแต่ละอนุภาคที่ชนกำแพงมันเป็นแบบไหนครับ เริ่มจากเราใช้สมมติฐานข้อที่ 2 มาตีความว่าการชนเป็นแบบยืดหยุ่น นั่นคือไม่มีการสูญเสียพลังงานจลน์หรือโมเมนตัม ดังนั้นมันก็แค่กลับทิศของความเร็วในแกนที่ชน เพื่อเขียนโปรแกรมเราต้องเช็คก่อนครับว่าอนุภาคมันหลุดขอบไปหรือยัง จากนั้นก็ใช้สูตรที่เราวิเคราะห์มานั่นคือ $x_{k+1,actual} = 2x_{bound}-x_{k+1}$ เพื่อคำนวณตำแหน่งที่อนุภาคควรอยู่จริง ๆ สุดท้ายเราค่อยเอาลบไปคูณความเร็วในแกนที่ชนก็จบแล้วครับ