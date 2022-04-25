# ws = " " * 4
ws = "	"


def dict_to_JSON(d: dict) -> str:  # only works for 1 dimensional dicts
	final: str = "{\n"
	for key, value in d.items():
		final += ws + '"' + key + '": ' + '"' + str(value) + "\",\n"
	final += "}"
	return final
