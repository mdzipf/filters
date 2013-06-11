displayName = "Isolate"
inputs=(("Block","blocktype"),)
def perform(level,box,options):
  for (chunk,slices,point) in level.getChunkSlices(box):
    blocks = chunk.Blocks[slices]
    blocks[blocks != options["Block"].ID] = 0
    chunk.chunkChanged()
