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