import sys
import os

# Add the curobo module to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..')))

# Import necessary libraries and modules
from curobo.cuda_robot_model.urdf_kinematics_parser import UrdfKinematicsParser

# Update these paths based on your findings
urdf_path = 'curobo/src/curobo/content/configs/robot/valkyrie_robot_config.yml'  # Adjust if necessary
mesh_root = 'curobo/src/curobo/content/assets/robot/iiwa_allegro_description/meshes'  # Adjust based on findings

# Initialize the URDF Kinematics Parser
parser = UrdfKinematicsParser(urdf_path, load_meshes=True, mesh_root=mesh_root)

# Build the link parent map
parser.build_link_parent()

# Example: Get the link parameters for a specific link
link_params = parser.get_link_parameters('base_link', base=True)

# Print the link parameters
print(link_params)

# Add absolute paths to link meshes
parser.add_absolute_path_to_link_meshes(mesh_dir=mesh_root)

# Get the URDF as a string
urdf_string = parser.get_urdf_string()
print(urdf_string)

# Get the controlled joint names
controlled_joint_names = parser.get_controlled_joint_names()
print(controlled_joint_names)

# Additional code to integrate with cuRobo, if necessary
