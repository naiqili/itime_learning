import os

class Config:
    def __init__(self, config_name="default"):

        self.recPath = "../RankSys/RankSys-examples/recommendations/100k/learning/"
        #self.seed2048Path = "../rival/rival-examples/data/ml-1m/seed2048/"
        #self.seed2048Path = "../itimerec/data/"
        self.seed2048Path = "../itime_rec/data/ml-100k/"
        #self.groundTruthPath = "../RankSys/RankSys-examples/recommendations/"
        self.groundTruthPath = "../RankSys/RankSys-examples/recommendations/100k/ground_truth/"
        
        if config_name == "default":
            self.get_default_config()
        elif config_name == "test":
            self.get_test_config()
        elif config_name == "simple_embed_test":
            self.get_simple_embed_test_config()
        elif config_name == "simple_embed_main":
            self.get_simple_embed_main_config()
        elif config_name == "simple_embed_main_with_feat":
            self.get_simple_embed_main_with_feat_config()
        elif config_name == "100k_data_prepare":
            self._100k_data_prepare_config()
        elif config_name == "100k_simple_embed_main_with_feat":
            self.get_100k_simple_embed_main_with_feat_config()
        elif config_name == "100k_embed_main_with_feat":
            self.get_100k_embed_main_with_feat_config()

        self.train_data_size = {}
        self.valid_data_size = {}
        self.train_data_user_size = {}
        self.valid_data_user_size = {}
        try:
            with open("%sfeat_size.txt" % self.datasizeDir) as f:
                n = f.readline().strip()
                self.feat_size = int(n)
            with open("%strain_size.txt" % self.datasizeDir) as f:
                for line in f:
                    cv, n = line.strip().split()
                    self.train_data_size[int(cv)] = int(n)
            with open("%svalid_size.txt" % self.datasizeDir) as f:
                for line in f:
                    cv, n = line.strip().split()
                    self.valid_data_size[int(cv)] = int(n)
            with open("%strain_user_size.txt" % self.datasizeDir) as f:
                for line in f:
                    cv, n = line.strip().split()
                    self.train_data_user_size[int(cv)] = int(n)
            with open("%svalid_user_size.txt" % self.datasizeDir) as f:
                for line in f:
                    cv, n = line.strip().split()
                    self.valid_data_user_size[int(cv)] = int(n)

            for _dir in [self.bestmodel_dir, self.log_dir, self.fig_path, self.ndcgConstantPath]:
                if not os.path.exists(_dir):
                    os.makedirs(_dir)

        except Exception, e:
            print e

    def get_default_config(self):
        self.user_size = 6040
        self.item_size = 3706
        # self.n_folds = 5
        self.n_folds = 5 # use 1 fold for testing & debugging

        self.recAlgos = ["pop", "ub", "ib", "hkv", "pzt", "plsa", "lda", "fm-bpr", "fm-rmse"]

        self.uifDir = "./data/main/uif/"
        self.iurDir = "./data/main/iur/"
        self.tfrecordDir = "./data/main/tfrecord/"
        self.datasizeDir = "./data/main/datasize/"

        # The paths are the uif/iur files to be loaded
        # during training (in LTRModel)
        # When trained on different folds, need to be changed
        # TODO: add valid
        self.train_uif_dir = "./data/main/uif/"
        self.train_iur_dir = "./data/main/iur/"
        # User test data for validation
        # TODO
        self.valid_uif_dir = "./data/main/uif/"
        self.valid_iur_dir = "./data/main/iur/"

        self.train_record_dir = "./data/main/tfrecord/"
        self.valid_record_dir = "./data/main/tfrecord/"
        #self.test_record_path = "./data/main/tfrecord/test_0.record"

        self.lr = 0.001 # learning rate
        self.z_size = 5

        self.max_step = 1000000
        self.patience = 5
        self.valid_freq = 2000
        self.train_freq = 1

        self.bestmodel_dir = "./model/basic/main/"
        self.log_dir = "./log/basic/main/"
        self.fig_path = "./log/basic/main/"

    def get_test_config(self):
        self.user_size = 500
        self.item_size = 500
        # self.n_folds = 5
        self.n_folds = 2 # use 2 fold for testing & debugging

        self.recAlgos = ["pop", "ub", "ib"]

        self.uifDir = "./data/test/uif/"
        self.iurDir = "./data/test/iur/"
        self.tfrecordDir = "./data/test/tfrecord/"
        self.datasizeDir = "./data/test/datasize/"

        # The paths are the uif/iur files to be loaded
        # during training (in LTRModel)
        # When trained on different folds, need to be changed
        # TODO: add valid
        self.train_uif_dir = "./data/test/uif/"
        self.train_iur_dir = "./data/test/iur/"
        # User test data for validation
        # TODO
        self.valid_uif_dir = "./data/test/uif/"
        self.valid_iur_dir = "./data/test/iur/"

        self.train_record_dir = "./data/test/tfrecord/"
        self.valid_record_dir = "./data/test/tfrecord/"
        #self.test_record_path = "./data/test/tfrecord/test_0.record"

        self.lr = 0.001 # learning rate
        self.z_size = 5

        self.max_step = 10000
        self.patience = 5
        self.valid_freq = 20
        self.train_freq = 1

        self.bestmodel_dir = "./model/basic/test/"
        self.log_dir = "./log/basic/test/"
        self.fig_path = "./log/basic/test/"

    def get_simple_embed_test_config(self):
        self.user_size = 500
        self.item_size = 500
        # self.n_folds = 5
        self.n_folds = 2 # use 2 fold for testing & debugging

        self.recAlgos = ["pop", "ub", "ib"]

        self.uifDir = "./data/test/uif/"
        self.iurDir = "./data/test/iur/"
        self.tfrecordDir = "./data/test/tfrecord/"
        self.datasizeDir = "./data/test/datasize/"

        self.lr = 0.001 # learning rate
        self.z_size = 5

        self.max_step = 10000
        self.patience = 5
        self.valid_freq = 20
        self.train_freq = 1

        self.bestmodel_dir = "./model/simple_embed/test/"
        self.log_dir = "./log/simple_embed/test/"
        self.fig_path = "./log/simple_embed/test/"

    def get_simple_embed_main_config(self):
        self.user_size = 6040
        self.item_size = 3706
        # self.n_folds = 5
        self.n_folds = 5 # use 1 fold for testing & debugging

        self.recAlgos = ["pop", "ub", "ib", "hkv", "pzt", "plsa", "lda", "fm-bpr", "fm-rmse"]

        self.uifDir = "./data/main/uif/"
        self.iurDir = "./data/main/iur/"
        self.tfrecordDir = "./data/main/tfrecord/"
        self.datasizeDir = "./data/main/datasize/"

        self.lr = 0.001 # learning rate
        self.z_size = 5

        self.max_step = 100000000
        self.patience = 5
        self.valid_freq = 20000
        self.train_freq = 1000

        self.bestmodel_dir = "./model/simple_embed/main/"
        self.log_dir = "./log/simple_embed/main/"
        self.fig_path = "./log/simple_embed/main/"

    def get_simple_embed_main_with_feat_config(self):
        self.user_size = 6040
        self.item_size = 3706
        # self.n_folds = 5
        self.n_folds = 5 # use 1 fold for testing & debugging

        self.recAlgos = ["pop", "ub", "ib", "hkv", "pzt", "plsa", "lda", "fm-bpr", "fm-rmse"]

        self.uifDir = "./data/main_feat/uif/"
        self.iurDir = "./data/main_feat/iur/"
        self.tfrecordDir = "./data/main_feat/tfrecord/"
        self.datasizeDir = "./data/main_feat/datasize/"

        self.lr = 0.001 # learning rate
        self.z_size = 5

        self.max_step = 100000000
        self.patience = 5
        self.valid_freq = 20000
        self.train_freq = 1000

        self.bestmodel_dir = "./model/simple_embed/main_feat/"
        self.log_dir = "./log/simple_embed/main_feat/"
        self.fig_path = "./log/simple_embed/main_feat/"

    def _100k_data_prepare_config(self):
        self.user_size = 777
        self.item_size = 516
        # self.n_folds = 5
        self.n_folds = 5 # use 1 fold for testing & debugging

        self.recAlgos = ["pop", "ub", "ib", "hkv", "pzt", "plsa", "lda", "fm-bpr", "fm-rmse"]

        self.uifDir = "./data/ml-100k/main_feat/uif/"
        #self.iurDir = "./data/ml-100k/main_feat/iur/"
        self.featMatDir = "./data/ml-100k/main_feat/featmat/"
        self.tfrecordDir = "./data/ml-100k/main_feat/tfrecord/"
        self.datasizeDir = "./data/ml-100k/main_feat/datasize/"

    def get_100k_simple_embed_main_with_feat_config(self):
        self.user_size = 777
        self.item_size = 516
        # self.n_folds = 5
        self.n_folds = 5 # use 1 fold for testing & debugging

        self.recAlgos = ["pop", "ub", "ib", "hkv", "pzt", "plsa", "lda", "fm-bpr", "fm-rmse"]

        self.uifDir = "./data/ml-100k/main_feat/uif/"
        self.iurDir = "./data/ml-100k/main_feat/iur/"
        self.tfrecordDir = "./data/ml-100k/main_feat/tfrecord/"
        self.datasizeDir = "./data/ml-100k/main_feat/datasize/"

        self.lr = 0.001 # learning rate
        self.z_size = 5

        self.max_step = 100000000
        self.patience = 5
        self.valid_freq = 20
        self.train_freq = 5

        self.bestmodel_dir = "./model/100k/simple_embed/main/"
        self.log_dir = "./log/100k/simple_embed/main/"
        self.fig_path = "./log/100k/simple_embed/main/"

    def get_100k_embed_main_with_feat_config(self):
        self.user_size = 777
        self.item_size = 516
        # self.n_folds = 5
        self.n_folds = 5 # use 1 fold for testing & debugging

        self.recAlgos = ["pop", "ub", "ib", "hkv", "pzt", "plsa", "lda", "fm-bpr", "fm-rmse"]

        self.uifDir = "./data/ml-100k/main_feat/uif/"
        self.tfrecordDir = "./data/ml-100k/main_feat/tfrecord/"
        self.datasizeDir = "./data/ml-100k/main_feat/datasize/"
        self.featMatDir = "./data/ml-100k/main_feat/featmat/"
        self.embedPath = "../itime_rec/embed/joint_pos/best/"

        self.lr = 0.001 # learning rate
        self.z_size = 5

        self.max_step = 100000000
        self.patience = 15
        self.valid_freq = 2000
        self.train_freq = 500

        self.bestmodel_dir = "./model/100k/embed/main/"
        self.log_dir = "./log/100k/embed/main/"
        self.fig_path = "./log/100k/embed/main/"
        self.ndcgConstantPath = "./data/ml-100k/ndcg_const/"

        self.drop_matrix = True
        self.drop_embed = True
