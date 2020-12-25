
Ó
u_ZN5cudnn6detail17wgrad_alg0_engineIfLi512ELi6ELi5ELi3ELi3ELi3ELb0ELi512EEEviiiPKT_iPS2_S4_18kernel_grad_paramsifiiii*28¦ÌÀ@¦ÌÀH¦ÌÀXb=gradient_tape/sequential/conv2d_1/Conv2D/Conv2DBackpropFilterh
q
:maxwell_scudnn_winograd_128x128_ldg1_ldg4_relu_tile148n_nt*28¸›Í@¸›ÍH¸›Íbsequential/conv2d_1/Reluh
’
5maxwell_scudnn_winograd_128x128_ldg1_ldg4_tile418n_nt*28ö·@ö·Hö·Xb<gradient_tape/sequential/conv2d_1/Conv2D/Conv2DBackpropInputh
ç
_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIKfSB_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEKNS_18TensorConversionOpIfKNS9_INS0_13scalar_cmp_opISB_SB_LNS0_14ComparisonNameE5EEESF_KNS_20TensorCwiseNullaryOpINS0_18scalar_constant_opISB_EESF_EEEEEEEEEENS_9GpuDeviceEEExEEvT_T0_*28¿ë€@¿ë€H¿ë€b*gradient_tape/sequential/conv2d_1/ReluGradh

1maxwell_scudnn_128x64_stridedB_splitK_interior_nn*28Ü«è@Ü«èHÜ«èXb=gradient_tape/sequential/conv2d_2/Conv2D/Conv2DBackpropFilterh

´_Z45pooling_bw_kernel_max_nchw_fully_packed_smallIffLi2EL21cudnnNanPropagation_t0EEv17cudnnTensorStructPKT_S1_S4_S1_S4_S1_PS2_18cudnnPoolingStructT0_S7_N5cudnn15reduced_divisorES9_*28ó²š@ó²šHó²šb:gradient_tape/sequential/max_pooling2d/MaxPool/MaxPoolGradh
’
5maxwell_scudnn_winograd_128x128_ldg1_ldg4_tile228n_nt*28®ûô@®ûôH®ûôXb<gradient_tape/sequential/conv2d_2/Conv2D/Conv2DBackpropInputh
Ñ
u_ZN5cudnn6detail17wgrad_alg0_engineIfLi512ELi6ELi5ELi3ELi3ELi3ELb1ELi512EEEviiiPKT_iPS2_S4_18kernel_grad_paramsifiiii*28¬°ã@¬°ãH¬°ãXb;gradient_tape/sequential/conv2d/Conv2D/Conv2DBackpropFilterh

1maxwell_scudnn_128x64_stridedB_splitK_interior_nn*28éÊÌ@éÊÌHéÊÌXb=gradient_tape/sequential/conv2d_3/Conv2D/Conv2DBackpropFilterh
q
:maxwell_scudnn_winograd_128x128_ldg1_ldg4_relu_tile418n_nt*28‰ãÊ@‰ãÊH‰ãÊbsequential/conv2d_2/Reluh
’
5maxwell_scudnn_winograd_128x128_ldg1_ldg4_tile418n_nt*28§„¸@§„¸H§„¸Xb<gradient_tape/sequential/conv2d_3/Conv2D/Conv2DBackpropInputh
å
_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIKfSB_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEKNS_18TensorConversionOpIfKNS9_INS0_13scalar_cmp_opISB_SB_LNS0_14ComparisonNameE5EEESF_KNS_20TensorCwiseNullaryOpINS0_18scalar_constant_opISB_EESF_EEEEEEEEEENS_9GpuDeviceEEExEEvT_T0_*28å½«@å½«Hå½«b(gradient_tape/sequential/conv2d/ReluGradh
j
2_ZN10tensorflow14BiasNCHWKernelIfEEviPKT_S3_PS1_ii*28½áê@½áêH½áêbsequential/conv2d/BiasAddh
ø
¸_ZN5cudnn6detail20pooling_fw_4d_kernelIffNS0_15maxpooling_funcIfL21cudnnNanPropagation_t0EEELi0ELb0EEEv17cudnnTensorStructPKT_S5_PS6_18cudnnPoolingStructT0_SB_iNS_15reduced_divisorESC_*28İˆå@İˆåHİˆåb sequential/max_pooling2d/MaxPoolh
ô
¾_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_max_opIKfSB_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEKNS_20TensorCwiseNullaryOpINS0_18scalar_constant_opISB_EESF_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28¹ŠË@¹ŠËH¹ŠËbsequential/conv2d/Reluh

´_Z45pooling_bw_kernel_max_nchw_fully_packed_smallIffLi2EL21cudnnNanPropagation_t0EEv17cudnnTensorStructPKT_S1_S4_S1_S4_S1_PS2_18cudnnPoolingStructT0_S7_N5cudnn15reduced_divisorES9_*28”¨¡@”¨¡H”¨¡b<gradient_tape/sequential/max_pooling2d_1/MaxPool/MaxPoolGradh
¿
k_ZN10tensorflow7functor15RowReduceKernelIPKfPfN3cub3SumEEEvT_T0_iiT1_NSt15iterator_traitsIS7_E10value_typeE*28ÓÁŸ@ÓÁŸHÓÁŸb5gradient_tape/sequential/conv2d_1/BiasAdd/BiasAddGradh
O
maxwell_sgemm_128x128_nn*28±æ„@±æ„H±æ„bsequential/conv2d_3/Reluh
à
£_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIffEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28Ê~@Ê~HÊ~b sequential/dropout/dropout/Mul_1h
î
£_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIffEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28°~@°~H°~b.gradient_tape/sequential/dropout/dropout/Mul_1h
\
&maxwell_scudnn_128x32_relu_interior_nn*28ï}@ï}Hï}Xbsequential/conv2d/Conv2Dh
º
k_ZN10tensorflow7functor15RowReduceKernelIPKfPfN3cub3SumEEEvT_T0_iiT1_NSt15iterator_traitsIS7_E10value_typeE*28‹¾]@‹¾]H‹¾]b3gradient_tape/sequential/conv2d/BiasAdd/BiasAddGradh
ä
_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIKfSB_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEKNS_18TensorConversionOpIfKNS9_INS0_13scalar_cmp_opISB_SB_LNS0_14ComparisonNameE5EEESF_KNS_20TensorCwiseNullaryOpINS0_18scalar_constant_opISB_EESF_EEEEEEEEEENS_9GpuDeviceEEExEEvT_T0_*28‹‰X@‹‰XH‹‰Xb*gradient_tape/sequential/conv2d_2/ReluGradh
â
™_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_18TensorCwiseUnaryOpINS0_11scalar_leftIffNS0_17scalar_product_opIffEELb0EEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEEEEENS_9GpuDeviceEEEiEEvT_T0_*28Š”W@Š”WHŠ”Wb,gradient_tape/sequential/dropout/dropout/Mulh
Ô
™_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_18TensorCwiseUnaryOpINS0_11scalar_leftIffNS0_17scalar_product_opIffEELb0EEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEEEEENS_9GpuDeviceEEEiEEvT_T0_*28ŠÚU@ŠÚUHŠÚUbsequential/dropout/dropout/Mulh

Z_ZN5cudnn17winograd_nonfused22winogradForwardData4x4IffEEvNS0_18WinogradDataParamsIT_T0_EE*28ê™O@ê™OHê™Obsequential/conv2d_3/Reluh
’
^_ZN5cudnn17winograd_nonfused24winogradForwardOutput4x4IffEEvNS0_20WinogradOutputParamsIT_T0_EE*28©ÑJ@©ÑJH©ÑJbsequential/conv2d_3/Reluh
Ü
ä_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_18TensorConversionOpIfKNS4_INS5_IKbLi1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28©ùF@©ùFH©ùFb[sequential/dropout/dropout/ArithmeticOptimizer/ReorderCastLikeAndValuePreserving_float_Casth
â
_ZN10tensorflow7functor28FillPhiloxRandomKernelLaunchINS_6random19UniformDistributionINS2_12PhiloxRandomEfEEEEvS4_PNT_17ResultElementTypeExS6_*28ÇÆ8@ÇÆ8HÇÆ8b7sequential/dropout/dropout/random_uniform/RandomUniformh
ä
_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIKfSB_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEKNS_18TensorConversionOpIfKNS9_INS0_13scalar_cmp_opISB_SB_LNS0_14ComparisonNameE5EEESF_KNS_20TensorCwiseNullaryOpINS0_18scalar_constant_opISB_EESF_EEEEEEEEEENS_9GpuDeviceEEExEEvT_T0_*28§´8@§´8H§´8b*gradient_tape/sequential/conv2d_3/ReluGradh
Ù
•_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIbLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_18TensorCwiseUnaryOpINS0_12scalar_rightIbfNS0_13greater_equalIfEELb0EEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEEEEENS_9GpuDeviceEEEiEEvT_T0_*28çß6@çß6Hçß6b'sequential/dropout/dropout/GreaterEqualh
¨
t_ZN10tensorflow7functor37SwapDimension1And2InTensor3UsingTilesIhLi256ELi32ELi32ELb0EEEvPKT_NS0_9DimensionILi3EEEPS2_*28‡š6@‡š6H‡š6b—gradient_tape/sequential/dropout/dropout/ArithmeticOptimizer/ReorderCastLikeAndValuePreserving_bool_Mul-1-TransposeNHWCToNCHW-LayoutOptimizer:Transposeh
¼
k_ZN10tensorflow7functor15RowReduceKernelIPKfPfN3cub3SumEEEvT_T0_iiT1_NSt15iterator_traitsIS7_E10value_typeE*28„³@„³H„³b5gradient_tape/sequential/conv2d_2/BiasAdd/BiasAddGradh
X
sgemm_32x32x32_TN_vec*28¤£@¤£H¤£b'gradient_tape/sequential/dense/MatMul_1h
K
sgemm_128x128x8_NN_vec*28ÃÀ@ÃÀHÃÀXbsequential/dense/MatMulh

<_ZN10tensorflow26BiasGradNCHW_SharedAtomicsIfEEvPKT_PS1_iiii*28ã×@ã×Hã×b5gradient_tape/sequential/conv2d_3/BiasAdd/BiasAddGradh
Y
sgemm_128x128x8_NT_vec*28£¯@£¯H£¯Xb%gradient_tape/sequential/dense/MatMulh
÷
¸_ZN5cudnn6detail20pooling_fw_4d_kernelIffNS0_15maxpooling_funcIfL21cudnnNanPropagation_t0EEELi0ELb0EEEv17cudnnTensorStructPKT_S5_PS6_18cudnnPoolingStructT0_SB_iNS_15reduced_divisorESC_*28Ã@ÃHÃb"sequential/max_pooling2d_1/MaxPoolh
Ö
™_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_18TensorCwiseUnaryOpINS0_11scalar_leftIffNS0_17scalar_product_opIffEELb0EEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEEEEENS_9GpuDeviceEEEiEEvT_T0_*28Ã”@Ã”HÃ”b sequential/dropout_1/dropout/Mulh
â
£_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIffEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28‚¤@‚¤H‚¤b"sequential/dropout_1/dropout/Mul_1h
ğ
£_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIffEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28‚@‚H‚b0gradient_tape/sequential/dropout_1/dropout/Mul_1h

t_ZN10tensorflow7functor37SwapDimension1And2InTensor3UsingTilesIhLi256ELi32ELi32ELb0EEEvPKT_NS0_9DimensionILi3EEEPS2_*28‚–@‚–H‚–bsequential/dropout_1/dropout/ArithmeticOptimizer/ReorderCastLikeAndValuePreserving_bool_Mul_1-0-TransposeNHWCToNCHW-LayoutOptimizer:Transposeh
ü
t_ZN10tensorflow7functor37SwapDimension1And2InTensor3UsingTilesIjLi256ELi32ELi32ELb0EEEvPKT_NS0_9DimensionILi3EEEPS2_*28Á†@Á†HÁ†blgradient_tape/sequential/max_pooling2d_1/MaxPool/MaxPoolGrad-2-TransposeNHWCToNCHW-LayoutOptimizer:Transposeh
ä
t_ZN10tensorflow7functor37SwapDimension1And2InTensor3UsingTilesIjLi256ELi32ELi32ELb0EEEvPKT_NS0_9DimensionILi3EEEPS2_*28¡ç
@¡ç
H¡ç
bTsequential/dropout_1/dropout/Mul_1-0-1-TransposeNCHWToNHWC-LayoutOptimizer:Transposeh
ä
™_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_18TensorCwiseUnaryOpINS0_11scalar_leftIffNS0_17scalar_product_opIffEELb0EEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEEEEENS_9GpuDeviceEEEiEEvT_T0_*28Áá	@Áá	HÁá	b.gradient_tape/sequential/dropout_1/dropout/Mulh
Ş
ä_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_18TensorConversionOpIfKNS4_INS5_IKbLi1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28ÁÎ@ÁÎHÁÎb]sequential/dropout_1/dropout/ArithmeticOptimizer/ReorderCastLikeAndValuePreserving_float_Casth
¢
ä_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_18TensorConversionOpIfKNS4_INS5_IKbLi1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28Í@ÍHÍb!sequential/dropout_1/dropout/Casth
Û
•_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIbLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_18TensorCwiseUnaryOpINS0_12scalar_rightIbfNS0_13greater_equalIfEELb0EEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEEEEENS_9GpuDeviceEEEiEEvT_T0_*28 ´@ ´H ´b)sequential/dropout_1/dropout/GreaterEqualh
V
sgemm_32x32x32_TN*28©@©H©b)gradient_tape/sequential/dense_3/MatMul_1h
L
sgemm_32x32x32_NN_vec*28”@”H”Xbsequential/dense_1/MatMulh
ä
_ZN10tensorflow7functor28FillPhiloxRandomKernelLaunchINS_6random19UniformDistributionINS2_12PhiloxRandomEfEEEEvS4_PNT_17ResultElementTypeExS6_*28¡@¡H¡b9sequential/dropout_1/dropout/random_uniform/RandomUniformh
Z
sgemm_32x32x32_TN_vec*28€õ@€õH€õb)gradient_tape/sequential/dense_1/MatMul_1h
Z
sgemm_32x32x32_TN_vec*28€ã@€ãH€ãb)gradient_tape/sequential/dense_2/MatMul_1h
[
sgemm_128x128x8_NT_vec*28 •@ •H •Xb'gradient_tape/sequential/dense_1/MatMulh
á
_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIKfSB_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEKNS_18TensorConversionOpIfKNS9_INS0_13scalar_cmp_opISB_SB_LNS0_14ComparisonNameE5EEESF_KNS_20TensorCwiseNullaryOpINS0_18scalar_constant_opISB_EESF_EEEEEEEEEENS_9GpuDeviceEEExEEvT_T0_*28àÙ@àÙHàÙb'gradient_tape/sequential/dense/ReluGradh
e
1_ZN10tensorflow14BiasNHWCKernelIfEEviPKT_S3_PS1_i*28¡Ì@¡ÌH¡Ìbsequential/dense/BiasAddh
ğ
¾_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_max_opIKfSB_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEKNS_20TensorCwiseNullaryOpINS0_18scalar_constant_opISB_EESF_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28 Å@ ÅH Åbsequential/dense/Reluh
Z
sgemm_32x32x32_NT_vec*28 ¸@ ¸H ¸Xb'gradient_tape/sequential/dense_2/MatMulh
ş
§_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_17TensorReductionOpINS0_10SumReducerIfEEKNS_5arrayIiLy1EEEKNS_18TensorForcedEvalOpIKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIKfSI_EEKNS_20TensorBroadcastingOpIKNSC_IxLy2EEEKNS4_INS5_ISI_Li2ELi1ExEELi16ES7_EEEEKNSG_INS0_20scalar_difference_opIffEEKNSK_IKNSC_IiLy2EEEKNSF_IKNS_18TensorCwiseUnaryOpINS0_13scalar_log_opIfEEKNS4_INS5_IfLi2ELi1ExEELi16ES7_EEEEEEEES11_EEEEEES7_EEEENS_9GpuDeviceEEExEEvT_T0_*28à«@à«Hà«b:categorical_crossentropy/softmax_cross_entropy_with_logitsh

O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28À…@À…HÀ…b$Adam/Adam/update_8/ResourceApplyAdamh
ˆ
:_ZN10tensorflow26BiasGradNHWC_SharedAtomicsIfEEviPKT_PS1_i*28á„@á„Há„b2gradient_tape/sequential/dense/BiasAdd/BiasAddGradh
ã
_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIKfSB_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEKNS_18TensorConversionOpIfKNS9_INS0_13scalar_cmp_opISB_SB_LNS0_14ComparisonNameE5EEESF_KNS_20TensorCwiseNullaryOpINS0_18scalar_constant_opISB_EESF_EEEEEEEEEENS_9GpuDeviceEEExEEvT_T0_*28áï@áïHáïb)gradient_tape/sequential/dense_1/ReluGradh
L
sgemm_32x32x32_NN_vec*28Àë@ÀëHÀëXbsequential/dense_2/MatMulh
H
sgemm_32x32x32_NN*28€Ì@€ÌH€ÌXbsequential/dense_3/MatMulh
¨
Ñ_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_17TensorReshapingOpIKNS_5arrayIiLy1EEENS_9TensorMapINS_6TensorIfLi2ELi1ExEELi16ENS_11MakePointerEEEEEKNS_17TensorReductionOpINS0_10MaxReducerIfEES7_KNS_20TensorBroadcastingOpIKNS5_IxLy2EEEKNS8_INS9_IKfLi2ELi1ExEELi16ESB_EEEESB_EEEENS_9GpuDeviceEEExEEvT_T0_*28 Æ@ ÆH Æb:categorical_crossentropy/softmax_cross_entropy_with_logitsh
V
sgemm_32x32x32_NT*28À½@À½HÀ½Xb'gradient_tape/sequential/dense_3/MatMulh
Ã
 _ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIxLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_20TensorTupleReducerOpINS0_18ArgMaxTupleReducerINS_5TupleIxfEEEEKNS_5arrayIxLy1EEEKNS4_INS5_IKfLi2ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28€¸@€¸H€¸bArgMaxh
Å
 _ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIxLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_20TensorTupleReducerOpINS0_18ArgMaxTupleReducerINS_5TupleIxfEEEEKNS_5arrayIxLy1EEEKNS4_INS5_IKfLi2ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28¡·@¡·H¡·bArgMax_1h
g
1_ZN10tensorflow14BiasNHWCKernelIfEEviPKT_S3_PS1_i*28 ¨@ ¨H ¨bsequential/dense_1/BiasAddh
ü
¥_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi2ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_20scalar_difference_opIffEEKNS9_INS0_18scalar_quotient_opIffEEKNS_18TensorCwiseUnaryOpINS0_13scalar_exp_opIfEEKS8_EEKNS_20TensorBroadcastingOpIKNS_5arrayIiLy2EEESH_EEEEKNSK_IKNSL_IxLy2EEEKNS4_INS5_IKfLi2ELi1ExEELi16ES7_EEEEEEEENS_9GpuDeviceEEExEEvT_T0_*28  @  H  b:categorical_crossentropy/softmax_cross_entropy_with_logitsh
š
Ã_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorEvalToOpIKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIKfS6_EEKNS_20TensorBroadcastingOpIKNS_5arrayIxLy2EEEKNS_9TensorMapINS_6TensorIS6_Li2ELi1ExEELi16ENS_11MakePointerEEEEEKNS4_INS0_20scalar_difference_opIffEEKNS8_IKNS9_IiLy2EEEKNS_18TensorForcedEvalOpIKNS_18TensorCwiseUnaryOpINS0_13scalar_log_opIfEEKNSC_INSD_IfLi2ELi1ExEELi16ESF_EEEEEEEESU_EEEESF_EENS_9GpuDeviceEEExEEvT_T0_*28À†@À†HÀ†b:categorical_crossentropy/softmax_cross_entropy_with_logitsh

»_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_17TensorReshapingOpIKNS_5arrayIiLy1EEENS_9TensorMapINS_6TensorIfLi2ELi1ExEELi16ENS_11MakePointerEEEEEKNS_17TensorReductionOpINS0_10SumReducerIfEES7_KNS_18TensorCwiseUnaryOpINS0_13scalar_exp_opIfEEKSC_EESB_EEEENS_9GpuDeviceEEExEEvT_T0_*28Àu@ÀuHÀub:categorical_crossentropy/softmax_cross_entropy_with_logitsh
»
n_ZN10tensorflow7functor18ColumnReduceKernelIPKfPfN3cub3SumEEEvT_T0_iiT1_NSt15iterator_traitsIS7_E10value_typeE*28 n@ nH nb4gradient_tape/sequential/dense_1/BiasAdd/BiasAddGradh
ï
¾_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_max_opIKfSB_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEKNS_20TensorCwiseNullaryOpINS0_18scalar_constant_opISB_EESF_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28 j@ jH jbsequential/dense_1/Reluh
à
_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIKfSB_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEKNS_18TensorConversionOpIfKNS9_INS0_13scalar_cmp_opISB_SB_LNS0_14ComparisonNameE5EEESF_KNS_20TensorCwiseNullaryOpINS0_18scalar_constant_opISB_EESF_EEEEEEEEEENS_9GpuDeviceEEExEEvT_T0_*28à^@à^Hà^b)gradient_tape/sequential/dense_2/ReluGradh
˜
²_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi2ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIffEEKNS4_INS5_IKfLi2ELi1EiEELi16ES7_EEKNS_20TensorBroadcastingOpIKNS_5arrayIxLy2EEESF_EEEEEENS_9GpuDeviceEEEiEEvT_T0_*28àW@àWHàWbLgradient_tape/categorical_crossentropy/softmax_cross_entropy_with_logits/mulh
º
†_ZN10tensorflow7functor15RowReduceKernelIN3cub22TransformInputIteratorIfNS_60_GLOBAL__N__36_softmax_op_gpu_cu_compute_70_cpp1_ii_4826c83b21SubtractAndExpFunctorIffEENS2_21CountingInputIteratorIixEExEEPfNS2_3SumEEEvT_T0_iiT1_NSt15iterator_traitsISC_E10value_typeE*28 Q@ QH Qbsequential/dense_3/Softmaxh

k_ZN10tensorflow7functor15RowReduceKernelIPKfPfN3cub3MaxEEEvT_T0_iiT1_NSt15iterator_traitsIS7_E10value_typeE*28€Q@€QH€Qbsequential/dense_3/Softmaxh
£
Ï_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi2ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_20scalar_difference_opIKfSB_EEKNS_20TensorBroadcastingOpIKNS_5arrayIxLy2EEEKNS4_INS5_ISB_Li2ELi1ExEELi16ES7_EEEEKNSD_IKNSE_IiLy2EEEKS8_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28àN@àNHàNb:categorical_crossentropy/softmax_cross_entropy_with_logitsh
¶
‚_ZN10tensorflow60_GLOBAL__N__36_softmax_op_gpu_cu_compute_70_cpp1_ii_4826c83b22GenerateNormalizedProbIffLi4EEEvPKT_PKT0_S4_PS2_iib*28 L@ LH Lbsequential/dense_3/Softmaxh
¼
n_ZN10tensorflow7functor18ColumnReduceKernelIPKfPfN3cub3SumEEEvT_T0_iiT1_NSt15iterator_traitsIS7_E10value_typeE*28 L@ LH Lb5gradient_tape/sequential/conv2d_1/BiasAdd/BiasAddGradh
¼
n_ZN10tensorflow7functor18ColumnReduceKernelIPKfPfN3cub3SumEEEvT_T0_iiT1_NSt15iterator_traitsIS7_E10value_typeE*28 L@ LH Lb5gradient_tape/sequential/conv2d_2/BiasAdd/BiasAddGradh
Œ
O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28ÀF@ÀFHÀFb$Adam/Adam/update_6/ResourceApplyAdamh
Œ
O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28 C@ CH Cb$Adam/Adam/update_4/ResourceApplyAdamh
d
1_ZN10tensorflow14BiasNHWCKernelIfEEviPKT_S3_PS1_i*28Á@@Á@HÁ@bsequential/dense_2/BiasAddh
”
c_ZN5cudnn8winograd27generateWinogradTilesKernelILi0EffEEvNS0_27GenerateWinogradTilesParamsIT0_T1_EE*28à<@à<Hà<bsequential/conv2d_1/Reluh
º
c_ZN5cudnn8winograd27generateWinogradTilesKernelILi0EffEEvNS0_27GenerateWinogradTilesParamsIT0_T1_EE*28à:@à:Hà:Xb<gradient_tape/sequential/conv2d_3/Conv2D/Conv2DBackpropInputh

^_ZN5cudnn17winograd_nonfused24winogradForwardFilter4x4IffEEvNS0_20WinogradFilterParamsIT_T0_EE*28€:@€:H€:bsequential/conv2d_3/Reluh
º
c_ZN5cudnn8winograd27generateWinogradTilesKernelILi0EffEEvNS0_27GenerateWinogradTilesParamsIT0_T1_EE*28€:@€:H€:Xb<gradient_tape/sequential/conv2d_1/Conv2D/Conv2DBackpropInputh
»
n_ZN10tensorflow7functor18ColumnReduceKernelIPKfPfN3cub3SumEEEvT_T0_iiT1_NSt15iterator_traitsIS7_E10value_typeE*28 9@ 9H 9b4gradient_tape/sequential/dense_2/BiasAdd/BiasAddGradh
”
c_ZN5cudnn8winograd27generateWinogradTilesKernelILi0EffEEvNS0_27GenerateWinogradTilesParamsIT0_T1_EE*28€9@€9H€9bsequential/conv2d_2/Reluh

O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28€8@€8H€8b%Adam/Adam/update_10/ResourceApplyAdamh
º
c_ZN5cudnn8winograd27generateWinogradTilesKernelILi0EffEEvNS0_27GenerateWinogradTilesParamsIT0_T1_EE*28 7@ 7H 7Xb<gradient_tape/sequential/conv2d_2/Conv2D/Conv2DBackpropInputh
¹
l_ZN10tensorflow7functor15CleanupSegmentsIPfS2_N3cub3SumEEEvT_T0_iiiT1_NSt15iterator_traitsIS5_E10value_typeE*28À5@À5HÀ5b4gradient_tape/sequential/dense_1/BiasAdd/BiasAddGradh
Œ
O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28€3@€3H€3b$Adam/Adam/update_2/ResourceApplyAdamh
»
n_ZN10tensorflow7functor18ColumnReduceKernelIPKfPfN3cub3SumEEEvT_T0_iiT1_NSt15iterator_traitsIS7_E10value_typeE*28 2@ 2H 2b4gradient_tape/sequential/dense_3/BiasAdd/BiasAddGradh
·
t_ZN10tensorflow7functor17BlockReduceKernelIPfS2_Li256ENS0_3SumIfEEEEvT_T0_iT2_NSt15iterator_traitsIS5_E10value_typeE*28à1@à1Hà1b*categorical_crossentropy/weighted_loss/Sumh
º
n_ZN10tensorflow7functor18ColumnReduceKernelIPKfPfN3cub3SumEEEvT_T0_iiT1_NSt15iterator_traitsIS7_E10value_typeE*28/@/H/b3gradient_tape/sequential/conv2d/BiasAdd/BiasAddGradh
d
1_ZN10tensorflow14BiasNHWCKernelIfEEviPKT_S3_PS1_i*28 .@ .H .bsequential/dense_3/BiasAddh
“
b_ZN10tensorflow7functor22ShuffleInTensor3SimpleIfLi2ELi1ELi0ELb0EEEviPKT_NS0_9DimensionILi3EEEPS2_*28à,@à,Hà,bsequential/conv2d_2/Reluh
Á
Ÿ_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIxLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_sum_opIxxEEKNS4_INS5_IKxLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28À+@À+HÀ+bAdam/addh
¹
b_ZN10tensorflow7functor22ShuffleInTensor3SimpleIfLi2ELi1ELi0ELb0EEEviPKT_NS0_9DimensionILi3EEEPS2_*28€+@€+H€+Xb<gradient_tape/sequential/conv2d_3/Conv2D/Conv2DBackpropInputh
º
l_ZN10tensorflow7functor15CleanupSegmentsIPfS2_N3cub3SumEEEvT_T0_iiiT1_NSt15iterator_traitsIS5_E10value_typeE*28€(@€(H€(b5gradient_tape/sequential/conv2d_1/BiasAdd/BiasAddGradh
º
l_ZN10tensorflow7functor15CleanupSegmentsIPfS2_N3cub3SumEEEvT_T0_iiiT1_NSt15iterator_traitsIS5_E10value_typeE*28à&@à&Hà&b5gradient_tape/sequential/conv2d_2/BiasAdd/BiasAddGradh
¹
l_ZN10tensorflow7functor15CleanupSegmentsIPfS2_N3cub3SumEEEvT_T0_iiiT1_NSt15iterator_traitsIS5_E10value_typeE*28 &@ &H &b4gradient_tape/sequential/dense_3/BiasAdd/BiasAddGradh
º
b_ZN10tensorflow7functor22ShuffleInTensor3SimpleIfLi2ELi1ELi0ELb0EEEviPKT_NS0_9DimensionILi3EEEPS2_*28à%@à%Hà%Xb=gradient_tape/sequential/conv2d_2/Conv2D/Conv2DBackpropFilterh
¹
b_ZN10tensorflow7functor22ShuffleInTensor3SimpleIfLi2ELi1ELi0ELb0EEEviPKT_NS0_9DimensionILi3EEEPS2_*28À%@À%HÀ%Xb<gradient_tape/sequential/conv2d_2/Conv2D/Conv2DBackpropInputh
“
b_ZN10tensorflow7functor22ShuffleInTensor3SimpleIfLi2ELi1ELi0ELb0EEEviPKT_NS0_9DimensionILi3EEEPS2_*28 %@ %H %bsequential/conv2d_3/Reluh
º
b_ZN10tensorflow7functor22ShuffleInTensor3SimpleIfLi2ELi1ELi0ELb0EEEviPKT_NS0_9DimensionILi3EEEPS2_*28 %@ %H %Xb=gradient_tape/sequential/conv2d_3/Conv2D/Conv2DBackpropFilterh
“
b_ZN10tensorflow7functor22ShuffleInTensor3SimpleIfLi2ELi1ELi0ELb0EEEviPKT_NS0_9DimensionILi3EEEPS2_*28à"@à"Hà"bsequential/conv2d_1/Reluh
¹
l_ZN10tensorflow7functor15CleanupSegmentsIPfS2_N3cub3SumEEEvT_T0_iiiT1_NSt15iterator_traitsIS5_E10value_typeE*28À"@À"HÀ"b4gradient_tape/sequential/dense_2/BiasAdd/BiasAddGradh

O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28 "@ "H "b%Adam/Adam/update_14/ResourceApplyAdamh
º
b_ZN10tensorflow7functor22ShuffleInTensor3SimpleIfLi2ELi1ELi0ELb0EEEviPKT_NS0_9DimensionILi3EEEPS2_*28 "@ "H "Xb=gradient_tape/sequential/conv2d_1/Conv2D/Conv2DBackpropFilterh

O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28  @  H  b%Adam/Adam/update_12/ResourceApplyAdamh
’
t_ZN10tensorflow7functor17BlockReduceKernelIPfS2_Li256ENS0_3SumIfEEEEvT_T0_iT2_NSt15iterator_traitsIS5_E10value_typeE*28 @ H bSum_2h
Š
O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28€@€H€b"Adam/Adam/update/ResourceApplyAdamh
¸
l_ZN10tensorflow7functor15CleanupSegmentsIPfS2_N3cub3SumEEEvT_T0_iiiT1_NSt15iterator_traitsIS5_E10value_typeE*28À@ÀHÀb3gradient_tape/sequential/conv2d/BiasAdd/BiasAddGradh
¹
b_ZN10tensorflow7functor22ShuffleInTensor3SimpleIfLi2ELi1ELi0ELb0EEEviPKT_NS0_9DimensionILi3EEEPS2_*28€@€H€Xb<gradient_tape/sequential/conv2d_1/Conv2D/Conv2DBackpropInputh
ï
¾_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_max_opIKfSB_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEKNS_20TensorCwiseNullaryOpINS0_18scalar_constant_opISB_EESF_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28 @ H bsequential/dense_2/Reluh
Á
Ÿ_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_pow_opIffEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28€@€H€bAdam/Powh
Ì
÷_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_20TensorBroadcastingOpIKNS_5arrayIiLy1EEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEEEEENS_9GpuDeviceEEEiEEvT_T0_*28 @ H b;gradient_tape/categorical_crossentropy/weighted_loss/Tile_1h
Œ
O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28 @ H b$Adam/Adam/update_9/ResourceApplyAdamh
ı
_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13div_no_nan_opIfEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28à@àHàbEgradient_tape/categorical_crossentropy/weighted_loss/value/div_no_nanh
Œ
O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28à@àHàb$Adam/Adam/update_3/ResourceApplyAdamh
Œ
O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28À@ÀHÀb$Adam/Adam/update_1/ResourceApplyAdamh
°
Ü_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorEvalToOpIKNS_18TensorCwiseUnaryOpINS0_13scalar_log_opIfEEKNS_9TensorMapINS_6TensorIfLi2ELi1ExEELi16ENS_11MakePointerEEEEESA_EENS_9GpuDeviceEEExEEvT_T0_*28 @ H b:categorical_crossentropy/softmax_cross_entropy_with_logitsh
·
˜_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIbLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_8equal_toIxEEKNS4_INS5_IKxLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28à@àHàbEqualh

O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28À@ÀHÀb%Adam/Adam/update_13/ResourceApplyAdamh

O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28À@ÀHÀb%Adam/Adam/update_15/ResourceApplyAdamh
¸
b_ZN10tensorflow7functor22ShuffleInTensor3SimpleIfLi2ELi1ELi0ELb0EEEviPKT_NS0_9DimensionILi3EEEPS2_*28À@ÀHÀXb;gradient_tape/sequential/conv2d/Conv2D/Conv2DBackpropFilterh

O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28 @ H b%Adam/Adam/update_11/ResourceApplyAdamh
Œ
O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28 @ H b$Adam/Adam/update_5/ResourceApplyAdamh
Œ
O_ZN10tensorflow7functor15ApplyAdamKernelIfEEviPT_S3_S3_PKS2_S5_S5_S5_S5_S5_S5_b*28 @ H b$Adam/Adam/update_7/ResourceApplyAdamh
{
H_ZN5cudnn7maxwell4gemm20computeOffsetsKernelENS1_20ComputeOffsetsParamsE*28€@€H€Xbsequential/conv2d/Conv2Dh
Ç
£_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIbLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_21scalar_boolean_and_opEKNS4_INS5_IKbLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28à@àHàb
LogicalAndh
¥
M_ZN5cudnn7maxwell4gemm25computeWgradOffsetsKernelENS1_20ComputeOffsetsParamsE*28à@àHàXb=gradient_tape/sequential/conv2d_3/Conv2D/Conv2DBackpropFilterh
Â
_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13div_no_nan_opIfEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28À@ÀHÀb
div_no_nanh
¥
M_ZN5cudnn7maxwell4gemm25computeWgradOffsetsKernelENS1_20ComputeOffsetsParamsE*28¡@¡H¡Xb=gradient_tape/sequential/conv2d_2/Conv2D/Conv2DBackpropFilterh
¢
J_ZN5cudnn7maxwell4gemm21computeBOffsetsKernelENS1_21ComputeBOffsetsParamsE*28€@€H€Xb=gradient_tape/sequential/conv2d_3/Conv2D/Conv2DBackpropFilterh
¶
ä_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_18TensorConversionOpIfKNS4_INS5_IKiLi1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28à@àHàb8categorical_crossentropy/weighted_loss/num_elements/Casth
‰
ä_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_18TensorConversionOpIfKNS4_INS5_IKxLi1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28à@àHàbAdam/Cast_1h
³
„_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_sum_opIKfSB_EEKS8_KNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28à@àHàbAssignAddVariableOp_2h
¢
J_ZN5cudnn7maxwell4gemm21computeBOffsetsKernelENS1_21ComputeBOffsetsParamsE*28à@àHàXb=gradient_tape/sequential/conv2d_2/Conv2D/Conv2DBackpropFilterh
”
<_Z24scalePackedTensor_kernelIffEv19cudnnTensor4dStructPT_T0_*28 @ H Xb=gradient_tape/sequential/conv2d_3/Conv2D/Conv2DBackpropFilterh
»
„_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIxLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_sum_opIKxSB_EEKS8_KNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28 @ H bAdam/Adam/AssignAddVariableOph
À
£_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_17scalar_product_opIffEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28€@€H€bMulh
³
„_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_sum_opIKfSB_EEKS8_KNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28€@€H€bAssignAddVariableOp_3h
”
<_Z24scalePackedTensor_kernelIffEv19cudnnTensor4dStructPT_T0_*28À@ÀHÀXb=gradient_tape/sequential/conv2d_2/Conv2D/Conv2DBackpropFilterh
Ã
Ÿ_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_pow_opIffEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28 @ H b
Adam/Pow_1h
³
„_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIxLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_sum_opIKxSB_EEKS8_KNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28 @ H bAssignAddVariableOp_4h
ä
_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13div_no_nan_opIfEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28€@€H€b,categorical_crossentropy/weighted_loss/valueh
•
b_ZN10tensorflow7functor22ShuffleInTensor3SimpleIfLi2ELi1ELi0ELb0EEEviPKT_NS0_9DimensionILi3EEEPS2_*28 @ H Xbsequential/conv2d/Conv2Dh
Ä
_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1EiEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13div_no_nan_opIfEEKNS4_INS5_IKfLi1ELi1EiEELi16ES7_EEKNS4_INS5_ISC_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28 @ H bdiv_no_nan_1h
„
ä_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_18TensorConversionOpIfKNS4_INS5_IKbLi1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28€@€H€bCast_1h
‚
ä_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_18TensorConversionOpIfKNS4_INS5_IKiLi1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28€@€H€bCasth
±
„_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_sum_opIKfSB_EEKS8_KNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28Á@ÁHÁbAssignAddVariableOph
„
ä_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_18TensorConversionOpIfKNS4_INS5_IKiLi1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28À@ÀHÀbCast_2h
³
„_ZN5Eigen8internal15EigenMetaKernelINS_15TensorEvaluatorIKNS_14TensorAssignOpINS_9TensorMapINS_6TensorIfLi1ELi1ExEELi16ENS_11MakePointerEEEKNS_19TensorCwiseBinaryOpINS0_13scalar_sum_opIKfSB_EEKS8_KNS4_INS5_ISB_Li1ELi1ExEELi16ES7_EEEEEENS_9GpuDeviceEEExEEvT_T0_*28À@ÀHÀbAssignAddVariableOp_1h