with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix immediateRender in theatrical-card ScrollTrigger
old_card_anim = """      gsap.utils.toArray('.theatrical-card').forEach((card, i) => {
        gsap.from(card, {
          scrollTrigger: {
            trigger: card,
            start: "top 88%",
            toggleActions: "play none none none"
          },
          y: 28,
          opacity: 0,
          duration: 0.75,
          ease: "power2.out",
          delay: (i % 3) * 0.1
        });
      });"""

new_card_anim = """      gsap.utils.toArray('.theatrical-card').forEach((card, i) => {
        gsap.from(card, {
          scrollTrigger: {
            trigger: card,
            start: "top 95%",
            toggleActions: "play none none none"
          },
          y: 24,
          opacity: 0,
          duration: 0.65,
          ease: "power2.out",
          immediateRender: false,
          delay: (i % 3) * 0.08
        });
      });"""

if old_card_anim in content:
    content = content.replace(old_card_anim, new_card_anim)
    print("Replaced theatrical-card animation with immediateRender: false")
else:
    print("Old card anim not matched exactly, checking regex...")

# 2. Richer opacity and tighter blur on morphing background shapes for vibrant presence
content = content.replace('stdDeviation="80"', 'stdDeviation="65"')
content = content.replace('stdDeviation="95"', 'stdDeviation="75"')
content = content.replace('stdDeviation="110"', 'stdDeviation="85"')
content = content.replace('id="morph-shape-primary"\n            class="morph-blob"\n            filter="url(#morph-blur-primary)"\n            fill="#2E1050"\n            opacity="0.32"', 'id="morph-shape-primary"\n            class="morph-blob"\n            filter="url(#morph-blur-primary)"\n            fill="#2E1050"\n            opacity="0.42"')
content = content.replace('id="morph-shape-secondary"\n            class="morph-blob"\n            filter="url(#morph-blur-secondary)"\n            fill="#D4A349"\n            opacity="0.34"', 'id="morph-shape-secondary"\n            class="morph-blob"\n            filter="url(#morph-blur-secondary)"\n            fill="#D4A349"\n            opacity="0.46"')
content = content.replace('id="morph-shape-tertiary"\n            class="morph-blob"\n            filter="url(#morph-blur-tertiary)"\n            fill="#FAF0D4"\n            opacity="0.25"', 'id="morph-shape-tertiary"\n            class="morph-blob"\n            filter="url(#morph-blur-tertiary)"\n            fill="#FAF0D4"\n            opacity="0.35"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Refinements applied successfully!")
