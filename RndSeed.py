class RndSeed:
#Random seed node for independent routing.    
	def __init__(self):
		pass
	
	@classmethod
	def INPUT_TYPES(s):
		return {
	  "required": {
		"seed": ("INT", {
		  "default": 1,
		  "min": -10,
		  "max": 9999999999999999
		}),
	  },
	}

	RETURN_TYPES = ("INT",)
	RETURN_NAMES = ("SEED",)
	FUNCTION = "main"
	CATEGORY = "image/RndSeed"

	def main(self, seed=0):
		return (seed,)

NODE_CLASS_MAPPINGS = {
	"Rndseed": RndSeed
}

#Display
NODE_DISPLAY_NAME_MAPPINGS = {
	"Rndseed": "Random Seed"
}