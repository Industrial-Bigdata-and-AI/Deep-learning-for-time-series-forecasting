from flood_forecast.custom.custom_opt import MASELoss, MAPELoss, RMSELoss, BertAdam
import unittest
import torch


class TestLossFunctions(unittest.TestCase):
    def setUp(self):
        self.mase = MASELoss("mean")

    def test_mase_runs(self):
        mase_input = torch.rand(2, 5, 1)
        mase_targ = torch.rand(2, 5, 1)
        mase_hist = torch.rand(2, 20, 20)
        self.mase(mase_input, mase_targ, mase_hist)

    def test_mase_mean_correct(self):
        m = MASELoss("mean")
        pred = torch.Tensor([2, 2]).repeat(2, 1)
        targ = torch.Tensor([4, 4]).repeat(2, 1)
        hist = torch.Tensor([6, 6]).repeat(2, 1)
        result = m(targ, pred, hist)
        self.assertEqual(result, 1)

    def test_mape_correct(self):
        m = MAPELoss()
        hist = torch.Tensor([7, 7]).repeat(2, 1)
        targ = torch.Tensor([4, 4]).repeat(2, 1)
        m(torch.rand(1, 3), torch.rand(1, 3))
        self.assertEqual(.75, m(hist, targ))

    def test_rmse_correct(self):
        pred = torch.Tensor([2, 2]).repeat(2, 1)
        targ = torch.Tensor([4, 4]).repeat(2, 1)
        r = RMSELoss()
        self.assertEqual(r(pred, targ), 2)

    def test_bert_adam(self):
        b_adam = BertAdam({"lr": 0.1})
        print(b_adam.get_lr)
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()