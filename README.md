# ExpressEar: Sensing Fine-Grained Facial Expressions with Earables

Continuous and unobtrusive monitoring of facial expressions holds tremendous potential to enable compelling applications in a multitude of domains ranging from healthcare and education to interactive systems. Traditional, vision-based facial expression recognition (FER) methods, however, are vulnerable to external factors like occlusion and lighting, while also raising privacy concerns coupled with the impractical requirement of positioning the camera in front of the user at all times. To bridge this gap, we propose ExpressEar, a novel FER system that repurposes commercial earables augmented with inertial sensors to capture fine-grained facial muscle movements. Following the Facial Action Coding System (FACS), which encodes every possible expression in terms of constituent facial movements called Action Units (AUs), ExpressEar identifies facial expressions at the atomic level. We conducted a user study (N=12) to evaluate the performance of our approach and found that ExpressEar can detect and distinguish between 32 Facial AUs (including 2 variants of asymmetric AUs), with an average accuracy of 89.9% for any given user. We further quantify the performance across different mobile scenarios in presence of additional face-related activities. Our results demonstrate ExpressEar's applicability in the real world and open up research opportunities to advance its practical adoption.

---

This repo contains the code for the experiments conducted in our paper. Kindly cite our paper if you use this code:

  Dhruv Verma, Sejal Bhalla, Dhruv Sahnan, Jainendra Shukla, and Aman Parnami. 2021. ExpressEar: Sensing Fine-Grained Facial Expressions with Earables. 
  Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. 5, 3, Article 129 (Sept 2021), 28 pages. DOI:https://doi.org/10.1145/3478085
