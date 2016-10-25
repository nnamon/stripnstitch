from PIL import Image

class StripNStitcher:

    def __init__(self, filename):
        self.image = Image.open(filename)

    def strip(self, position, width=1):
        tempim = self.image.crop((position, 0, position+width,
                                  self.image.height))
        return tempim

    def stitch(self, tempim):
        newim = Image.new(self.image.mode, (self.image.height,)*2)
        data = []
        for i in tempim.getdata():
            for j in range(tempim.height):
                data.append(i)
        newim.putdata(data)
        return newim

    def stripnstitch(self, position):
        simage = self.strip(position)
        nimage = self.stitch(simage)
        return nimage

def main():
    sns = StripNStitcher("./samples/pepe.png")
    sns.stripnstitch(196).save("./samples/output.png")

if __name__  == "__main__":
    main()
