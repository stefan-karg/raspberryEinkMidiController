import eink
display = eink.Eink()

display.init()
display.text("Hello World")
display.text("Hello Moon", x=35, y=25)
display.update()
