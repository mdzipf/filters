import pymclevel

displayName = "Make Solid"
inputs = (
    ("Direction", ("Down","Up")),
    ("Block", "blocktype")
    )

def perform(level, box, options):
  for x in xrange(box.minx, box.maxx):
    for z in xrange(box.minz, box.maxz):
      if options["Direction"] == "Down":
        yrange=xrange(box.miny,box.maxy)
      else:
        yrange=xrange(box.maxy,box.miny,-1)
      for y in yrange:
        if level.blockAt(x, y, z) != 0:
          print "Isn't air!"
          if options["Direction"] == "Down":
            fillrange=xrange(box.miny,y)
          else:
            fillrange=xrange(y+1,box.maxy)
          for i in fillrange:
            level.setBlockAt(x, i, z, options["Block"].ID)
          break
