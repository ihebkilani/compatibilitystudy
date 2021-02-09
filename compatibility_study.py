import numpy as np 
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity

class Compatibility_study():
    t1_A = 0
    t2_A = 0
    t1_B = 0
    t2_B = 0

    def __init__(self, t1_A, t2_A, t1_B, t2_B):
        self.t1_A = t1_A
        self.t2_A = t2_A
        self.t1_B = t1_B
        self.t2_B = t2_B

    def rotation_matrix(self, theta):
        angle = np.radians(theta) 
        c, s = np.cos(angle), np.sin(angle)
        return np.array(((c, -s), (s, c)))
        
    def compatibility(self):
        user_a_traits = np.array((float(self.t1_A), float(self.t2_A)))
        R = self.rotation_matrix(30)
        rot_user_a_traits = np.dot(R,user_a_traits)
        opt_user_traits = np.array((rot_user_a_traits[0],-rot_user_a_traits[1]))
        user_b_traits = np.array((float(self.t1_B), float(self.t2_B)))
        opt_user_traits = opt_user_traits.reshape(1,-1)
        user_b_traits = user_b_traits.reshape(1,-1)
        cos_similarity = cosine_similarity(user_b_traits,opt_user_traits)
        angular_distance = np.arccos(cos_similarity)/np.pi
        angular_similarity = 1 - angular_distance
        return angular_similarity