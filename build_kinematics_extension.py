from torch.utils.cpp_extension import load
import os

# Define paths to source files
src_dir = '/home/weston/curobo/src/curobo/curobolib/cpp'
source_files = [
    os.path.join(src_dir, 'kinematics_fused_cuda.cpp'),
    os.path.join(src_dir, 'kinematics_fused_kernel.cu')
]

# Build and load the extension
kinematics_fused_cu = load(
    name='kinematics_fused_cu',
    sources=source_files,
    verbose=True
)



