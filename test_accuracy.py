import json
from collections import Counter

def calculate_accuracy(predictions_file):
    """
    从predictions.jsonl文件计算正确率和其他统计信息
    """
    correct = 0
    total = 0
    confidences = []
    predictions = []
    
    with open(predictions_file, 'r') as f:
        for line in f:
            result = json.loads(line)
            if 'actual' in result and 'predicted' in result:
                total += 1
                if result['actual'] == result['predicted']:
                    correct += 1
                confidences.append(result['confidence'])
                predictions.append(result['predicted'])
    
    accuracy = correct / total if total > 0 else 0
    avg_confidence = sum(confidences) / len(confidences) if confidences else 0
    
    # 计算每个选项的分布
    pred_distribution = Counter(predictions)
    
    print(f"\n=== 评估结果 ===")
    print(f"总样本数: {total}")
    print(f"正确数量: {correct}")
    print(f"正确率: {accuracy:.2%}")
    print(f"平均置信度: {avg_confidence:.3f}")
    print("\n预测分布:")
    for option, count in pred_distribution.items():
        print(f"选项 {option}: {count} ({count/total:.2%})")
    
    return {
        'total_samples': total,
        'correct_predictions': correct,
        'accuracy': accuracy,
        'avg_confidence': avg_confidence,
        'prediction_distribution': dict(pred_distribution)
    }


predictions_file = "predictions/test_0.6.jsonl"
metrics = calculate_accuracy(predictions_file)
