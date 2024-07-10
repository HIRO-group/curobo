import os
import torch
import xacro
from curobo.cuda_robot_model.urdf_kinematics_parser import UrdfKinematicsParser
from curobo.cuda_robot_model.kinematics_parser import LinkParams
from curobo.cuda_robot_model.cuda_robot_generator import TensorDeviceType, CudaRobotGeneratorConfig, CudaRobotGenerator
from curobo.util_file import get_assets_path, join_path
from torch.utils.cpp_extension import load

# Ensure this import is included
kinematics_fused_cu = load(
    name="kinematics_fused_cu",
    sources=[
        "/home/weston/curobo/src/curobo/curobolib/cpp/kinematics_fused_cuda.cpp",
        "/home/weston/curobo/src/curobo/curobolib/cpp/kinematics_fused_kernel.cu"
    ],
    verbose=True
)

# Function to process xacro file into URDF string
def get_urdf_from_xacro(xacro_path):
    urdf_string = xacro.process_file(xacro_path).toxml()
    return urdf_string

# Path to your xacro file
xacro_path = "/home/weston/curobo/src/curobo/content/assets/robot/franka_description/franka_panda.urdf"

# Generate URDF string from xacro file
urdf_string = get_urdf_from_xacro(xacro_path)

# Define the configuration for the CudaRobotGenerator
config = CudaRobotGeneratorConfig(
    base_link="panda_link0",
    ee_link="panda_link8",
    tensor_args=TensorDeviceType(),
    urdf_path=urdf_string,
    # Add other necessary parameters here
)

# Initialize the CUDA robot generator
robot_generator = CudaRobotGenerator(config)

# Perform necessary operations with the robot_generator
# Save the configuration or model as needed
output_path = "/home/weston/curobo/generated_robot_model.pt"
torch.save(robot_generator, output_path)
