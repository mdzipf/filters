import pymclevel

displayName = "Mob Spout"

inputs = (
    ("X offset", 0),
    ("Y offset", 10),
    ("Z offset", 0),
    ("Tick Delay",1),
    ("Detection Range",16),
    ("Mob",tuple(pymclevel.Entity.monsters))
)

def perform(level, box, options):
  Xoff, Yoff, Zoff = options["X offset"], options["Y offset"], options["Z offset"]
  delay = options["Tick Delay"]
  dest = ((box.minx+box.maxx)/2+Xoff,
          (box.miny+box.maxy)/2+Yoff,
          (box.minz+box.maxz)/2+Zoff)
  for x in range(box.minx, box.maxx):
    for y in range(box.miny, box.maxy):
      for z in range(box.minz, box.maxz):
        entity = pymclevel.TAG_Compound()
        entity["id"] = options["Mob"]
        entity["Pos"]=pymclevel.TAG_List()
        for i in dest:
          entity["Pos"].append(pymclevel.TAG_Double(i))
        level.setBlockAt(x, y, z, 52)
        level.setBlockDataAt(x, y, z, 0)
        spawner = pymclevel.TileEntity.Create("MobSpawner")
        spawner["Delay"] = pymclevel.TAG_Short(delay)
        spawner["MinSpawnDelay"] = pymclevel.TAG_Short(delay)
        spawner["MaxSpawnDelay"] = pymclevel.TAG_Short(delay)
        spawner["SpawnCount"] = pymclevel.TAG_Short(1)
        spawner["MaxNearbyEntities"] = pymclevel.TAG_Short(10000)
        spawner["RequiredPlayerRange"] = pymclevel.TAG_Short(options["Detection Range"])
        spawner["SpawnData"]=entity
        spawner["EntityId"]=entity["id"]
        pymclevel.TileEntity.setpos(spawner,(x,y,z))
        for chunk,slices,point in level.getChunkSlices(box):
          if chunk.containsPoint(x,y,z):
            chunk.TileEntities.append(spawner)
