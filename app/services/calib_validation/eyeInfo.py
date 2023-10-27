import random
import csv
import tkinter as tk

class EyeInfo:
    def __init__(self, right_eye =[], left_eye=[], prediction=[], calib_points=[], dataset='./data.csv', screen_width=0, screen_height=0, k_screen_width = 1872, k_screen_height = 944):
            self.right_eye = right_eye
            self.left_eye = left_eye
            self.prediction = prediction
            self.calib_points = calib_points
            self.dataset = dataset
            self.screen_width = screen_width
            self.screen_height = screen_height
            self.k_screen_width = k_screen_width
            self.k_screen_height = k_screen_height

    def init_calib_points(self):
        if self.calib_points:
            self.init_screen_resolution()
            # m_factorx = self.screen_width/self.k_screen_width
            # m_factory = self.screen_height/self.k_screen_height
            post_calib = []
            for point in self.calib_points:
                calibrated_point = {
                    "x": point["x"],
                    "y": point["y"]
                }
                post_calib.append(calibrated_point)

            self.calib_points = post_calib

    

    def init_screen_resolution(self):
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        root.destroy()


    def init_points(self):
        self.init_screen_resolution()
        # m_factorx = self.screen_width/self.k_screen_width
        # m_factory = self.screen_height/self.k_screen_height
        try:
            with open(self.dataset, 'r', newline='') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    right_eye_point = {
                        'x': float(row['right_iris_x']),
                        'y': float(row['right_iris_y'])
                    }
                    self.right_eye.append(right_eye_point)

                    left_eye_point = {
                        'x': float(row['left_iris_x']),
                        'y': float(row['left_iris_y'])
                    }
                    self.left_eye.append(left_eye_point)
                    x =float(row['screen_x'])
                    y =float(row['screen_y'])
                    prediction_point = {
                        'x':float(row['screen_x']),
                        'y':float(row['screen_y'])
                    }
                    self.prediction.append(prediction_point)

        
        
        except FileNotFoundError:
            print(f"File {self.dataset} not found.")
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {str(e)}")

    def get_right_eye(self):
        right_x_values = []
        right_y_values = []
        for item in self.right_eye:
            right_x_values.append(item['x'])
            right_y_values.append(item['y'])
        return right_x_values, right_y_values
    
    def get_left_eye(self):
        left_x_values = []
        left_y_values = []
        for item in self.left_eye:
            left_x_values.append(item['x'])
            left_y_values.append(item['y'])
        return left_x_values, left_y_values
    
    def get_predictions(self):
        predict_x_values = []
        predict_y_values = []
        for item in self.prediction:
            predict_x_values.append(item['x'])
            predict_y_values.append(item['y'])
        return predict_x_values, predict_y_values
    
    def get_calib(self):
        calib_x_values = []
        calib_y_values = []
        for item in self.calib_points:
            calib_x_values.append(item['x'])
            calib_y_values.append(item['y'])
        return calib_x_values, calib_y_values 
  
    def randomize_points(self, num_objects):
        objects_right = []
        objects_left = []
        objects_prediction = []
        for _ in range(num_objects):
            obj = {'x': random.randint(0, 1536), 'y': random.randint(0, 864)}
            objects_right.append(obj)
        for _ in range(num_objects):
            obj = {'x': random.randint(0, 1536), 'y': random.randint(0, 864)}
            objects_left.append(obj)
        
        for _ in range(num_objects):
            obj = {'x': random.randint(0, 1536), 'y': random.randint(0, 864)}
            objects_left.append(obj)

        self.right_eye = objects_right
        self.left_eye = objects_left
        self.prediction = objects_prediction

