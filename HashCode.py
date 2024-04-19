
import hashlib

def convert(data = 'sajid24x4@gmail.com'):
	hash_value = hashlib.md5(data.encode()).hexdigest()
	print(hash_value+"")
	return hash_value


if __name__ == '__main__':
	convert("ali@gmail.com")