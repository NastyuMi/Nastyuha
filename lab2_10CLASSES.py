class cream:
	text_for_cream= "types of creams:"

	def its(self):
		print(self.text_for_cream)

class skin_cream(cream):
	texy_for_skin_cream = "skin cream"

	def its_s(self):
		print(f"1. {self.texy_for_skin_cream}")

class hand_cream(cream):
	text_for_hand_cream = "hand cream"

	def its_h(self):
		print(f"2. {self.text_for_hand_cream}")

class body_cream(cream):
	text_for_body_cream = "body cream"

	def its_b(self):
		print(f"3. {self.text_for_body_cream}")

class foot_cream(cream):
	text_for_foot_cream= "foot cream"

	def its_f(self):
		print(f"4. {self.text_for_foot_cream}")

class face_cream(cream):
	text_for_face_cream = "face cream"

	def its_face(self):
		print(f"5. {self.text_for_face_cream}")

class eye(face_cream):
	text_for_eye = "eye cream"

	def its_eye(self):
		print(f"   a. {self.text_for_eye}")

class anti_wrinkle(eye):
	text_for_anti_wrinkle = "anti-wrinkle cream"

	def its_anti_wrinkle(self):
		self.its_face()
		self.its_eye()
		print(f"      -  {self.text_for_anti_wrinkle}")

class lip(face_cream):
	text_for_lip = "lip cream"

	def its_lip(self):
		print(f"   b. {self.text_for_lip}")

class body_scrub(body_cream):
	text_for_body_scrub = "body scrub"

	def its_b_s(self):
		self.its_b()
		print(f"   a. {self.text_for_body_scrub}")




cream = cream()
cream.its()

skin = skin_cream()
skin.its_s()

hand = hand_cream()
hand.its_h()

body = body_scrub()
body.its_b_s()

foot = foot_cream()
foot.its_f()

face = anti_wrinkle()
face.its_anti_wrinkle()

lip= lip()
lip.its_lip()
