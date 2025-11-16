# SimpleTranslateNode 使用示例

## 基本使用方法

1. 在ComfyUI中添加"简单翻译"节点
2. 设置select_index为1-5之间的数字
3. 在对应的文本框中输入内容
4. 根据需要开启或关闭翻译功能

## 示例配置

### 示例1：基本文本选择
- select_index: 2
- text_1: 这是第一段文本
- text_2: 这是第二段文本（将被选中）
- text_3: 这是第三段文本
- text_4: 这是第四段文本
- text_5: 这是第五段文本
- translate_text: false

输出：这是第二段文本

### 示例2：带注释的文本
- select_index: 1
- text_1: 
  ```
  # 这是一个注释行，将被删除
  这是实际内容的第一行
  # 这是另一个注释行
  这是实际内容的第二行
  ```
- translate_text: false

输出：
```
这是实际内容的第一行
这是实际内容的第二行
```

### 示例3：翻译功能
- select_index: 3
- text_3: 
  ```
  这是一段中文文本
  将被翻译成英文
  ```
- translate_text: true

输出：
```
This is a Chinese text
Will be translated into English
```

## 注意事项

1. 翻译功能默认将中文翻译为英文
2. 所有以#开头的行将被视为注释并自动删除
3. 如果索引超出1-5的范围，将自动调整为最近的边界值