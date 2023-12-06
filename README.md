# HeteroFL: Computation and Communication Efficient Federated Learning for Heterogeneous Clients

## Requirements

- see requirements.txt

## Instruction

- Global hyperparameters are configured in config.yml
- Hyperparameters can be found at process_control() in utils.py
- fed.py contrains aggregation and separation of subnetworks

## Examples

- Train MNIST dataset (IID) with CNN model, 100 users, active rate 0.1, model split 'Fix', model split mode 'a-b (20%-80%)', BatchNorm, Scaler (True) , Masked CrossEntropy (True)
  ```ruby
  python3 train_classifier_fed.py --data_name MNIST --model_name conv --control_name 1_100_0.1_iid_fix_a2-b8_bn_1_1
  ```
- Train CIFAR10 dataset (Non-IID 2 classes) with ResNet model, 10 users, active rate 0.1, model split 'Dynamic', model split mode 'a-b-c (uniform)', GroupNorm, Scaler (False) , Masked CrossEntropy (False)
  ```ruby
  python3 train_classifier_fed.py --data_name CIFAR10 --model_name resnet18 --control_name 1_10_0.1_non-iid-2_dynamic_a1-b1-c1_gn_0_0
  ```
- Test WikiText2 dataset with Transformer model, 100 users, active rate 0.01, model split 'Fix', model split mode 'a (50%), b(50%)', No Normalization, Scaler (True) , Masked CrossEntropy (False)
  ```ruby
  python3 test_transformer_fed.py --data_name WikiText2 --model_name transformer --control_name 1_100_0.01_iid_fix_a5-b5_none_1_0
  ```
