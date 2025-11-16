"""
Simple Translate Node for ComfyUI
根据输入的整数选择对应的文本，支持翻译开关控制
"""
import argostranslate.translate

class SimpleTranslate:
    """
    数字到文本映射节点    输入：一个整数（1-5）和5个文本和翻译开关    输出：根据整数选择的文本（可选翻译）
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        """定义节点的输入参数"""
        return {
            "required": {
                "select_index": ("INT", {"default": 1, "min": 1, "max": 5, "step": 1, "display": "number"}),
                "text_1": ("STRING", {"default": "", "multiline": True, "placeholder": "输入文本1"}),
                "text_2": ("STRING", {"default": "", "multiline": True, "placeholder": "输入文本2"}),
                "text_3": ("STRING", {"default": "", "multiline": True, "placeholder": "输入文本3"}),
                "text_4": ("STRING", {"default": "", "multiline": True, "placeholder": "输入文本4"}),
                "text_5": ("STRING", {"default": "", "multiline": True, "placeholder": "输入文本5"}),
                "translate_text": ("BOOLEAN", {"default": True, "label_on": "翻译", "label_off": "不翻译"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("输出文本",)
    FUNCTION = "select_text"
    CATEGORY = "SimpleTranslate"
    
    def select_text(self, select_index, text_1, text_2, text_3, text_4, text_5, translate_text):
        """
        根据选择的索引返回对应的文本，可选择是否翻译
        
        参数:
            select_index: 选择的索引（1-5）
            text_1-text_5: 5个文本输入
            translate_text: 是否翻译文本的开关
        返回:
            根据索引选择的文本（删除所有以'#'开头的行，根据开关决定是否翻译剩余内容）
        """
        # 创建文本映射字典
        text_map = {
            1: text_1,
            2: text_2,
            3: text_3,
            4: text_4,
            5: text_5
        }
        
        # 确保索引在有效范围内
        if select_index < 1:
            select_index = 1
        elif select_index > 5:
            select_index = 5
        
        # 获取选中的文本
        selected_text = text_map[select_index]
        
        # 处理所有行，删除以'#'开头的行
        lines = selected_text.split('\n')
        processed_lines = []
        for line in lines:
            if not line.strip().startswith('#'):
                processed_lines.append(line)
        
        # 根据开关决定是否翻译文本
        if translate_text:
            # 翻译处理后的非注释行
            translated_lines = []
            for line in processed_lines:
                translated_lines.append(argostranslate.translate.translate(line, 'zh', 'en'))
            result_text = '\n'.join(translated_lines)
        else:
            # 不翻译，直接返回非注释行
            result_text = '\n'.join(processed_lines)
        
        # 返回单一输出文本
        return (result_text,)

# 节点映射
NODES = {
    "SimpleTranslate": SimpleTranslate
}
