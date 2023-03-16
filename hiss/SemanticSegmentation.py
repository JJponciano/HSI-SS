from hiss.keras_segmentation.models.pspnet import pspnet
from hiss import keras_segmentation as predict


class SemanticSegmentation:
    def __init__(self, model_class='pspnet', num_classes=51, channel=3, epochs=20, input_height=192, input_width=192,path=None, best_size=True):
        if best_size:
            # compute the euclidian divition (without the rest and multiply by 192, a requirement for pspnet is to be a multiple of 192
            self.input_height = int(input_height/192)*192
            self.input_width = int(input_width/192)*192
        else:
            self.input_height = input_height
            self.input_width = input_width
        self.model_class = model_class
        self.num_classes = num_classes
        self.channel = channel
        self.epochs = epochs

        self.model = pspnet(n_classes=self.num_classes , input_height=self.input_height, input_width=self.input_width, channels=self.channel)
        if path is not None:
            self.path=path
        else:
            self.path = self.model_class+ str(input_height)+"_"+ str(input_width)+".h5"

    def train(self,train_dir_img,train_dir_annotations):
        self.model.train(train_images=train_dir_img, train_annotations=train_dir_annotations, epochs=self.epochs)
        self.model.save(self.path)
        return self.path

    def load(self,path):
        model_config = {
            "input_height": self.input_height,
            "input_width": self.input_width,
            "n_classes": self.num_classes,
            "model_class": self.model_class
        }
        self.model = model_from_checkpoint_path(model_config=model_config, latest_weights=path)

    def evaluation(self,img_dir,annotations_dir):
        return self.model.evaluate_segmentation(inp_images_dir=img_dir, annotations_dir=annotations_dir)

    def prediction(self,input_dir,output_dir):
        predict.predict_multiple(self.model, inp_dir=input_dir, out_dir=output_dir)

