export MODEL_NAME="lambdalabs/sd-image-variations-diffusers"
export MODEL_NAME="runwayml/stable-diffusion-v1-5"
export OUTPUT_DIR="weights/finetuned_emojis_2"
export DATASET_NAME="data/emojis/emojisdescr.hf/train/data-00000-of-00001.arrow"


accelerate launch --mixed_precision="fp16"  3rd/diffusers/examples/text_to_image/train_text_to_image_lora.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --dataset_name=$DATASET_NAME \
  --dataloader_num_workers=8 \
  --resolution=512 --center_crop --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --max_train_steps=5000 \
  --learning_rate=1e-04 \
  --max_grad_norm=1 \
  --lr_scheduler="cosine" --lr_warmup_steps=0 \
  --output_dir=${OUTPUT_DIR} \
  --checkpointing_steps=500 \
  --validation_prompt="A face of evil gnome." \
  --seed=1337

