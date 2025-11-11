# Ardur Technology Design System

## Overview

The Ardur Technology design system is built on modern principles of accessibility, performance, and visual excellence. It combines the utility-first approach of Tailwind CSS with custom design tokens to create a cohesive, professional, and trustworthy brand experience.

## Color Palette

### Primary Colors

Our primary color palette uses vibrant, modern colors that convey trust, innovation, and growth:

#### Primary Green (`primary`)
- **50**: `#f0fdf4` - Very light tint
- **100**: `#dcfce7` - Light tint
- **200**: `#bbf7d0` - Light
- **300**: `#86efac` - Medium light
- **400**: `#4ade80` - Medium
- **500**: `#22c55e` - **Base primary color**
- **600**: `#16a34a` - Medium dark
- **700**: `#15803d` - Dark
- **800**: `#166534` - Very dark
- **900**: `#14532d` - Darkest

#### Secondary Teal (`secondary`)
- **50**: `#f0fdfa`
- **100**: `#ccfbf1`
- **200**: `#99f6e4`
- **300**: `#5eead4`
- **400**: `#2dd4bf`
- **500**: `#14b8a6` - **Base secondary color**
- **600**: `#0d9488`
- **700**: `#0f766e`
- **800**: `#115e59`
- **900**: `#134e4a`

#### Accent Blue (`accent`)
- **50**: `#eff6ff`
- **100**: `#dbeafe`
- **200**: `#bfdbfe`
- **300**: `#93c5fd`
- **400**: `#60a5fa`
- **500**: `#3b82f6` - **Base accent color**
- **600**: `#2563eb`
- **700**: `#1d4ed8`
- **800**: `#1e40af`
- **900**: `#1e3a8a`

#### Warning Amber (`warning`)
- **50**: `#fffbeb`
- **100**: `#fef3c7`
- **200**: `#fde68a`
- **300**: `#fcd34d`
- **400**: `#fbbf24`
- **500**: `#f59e0b` - **Base warning color**
- **600**: `#d97706`
- **700**: `#b45309`
- **800**: `#92400e`
- **900**: `#78350f`

#### Purple (`purple`)
- **50**: `#faf5ff`
- **100**: `#f3e8ff`
- **200**: `#e9d5ff`
- **300**: `#d8b4fe`
- **400**: `#c084fc`
- **500**: `#a855f7` - **Base purple color**
- **600**: `#9333ea`
- **700**: `#7c3aed`
- **800**: `#6b21a8`
- **900**: `#581c87`

### Neutral Colors

We use Tailwind's default gray palette for neutral elements:
- **Gray 50-900**: For backgrounds, text, and UI elements
- **White**: `#ffffff` - Pure white for backgrounds
- **Black**: `#000000` - For high contrast text (rarely used)

### Gradients

#### Primary Gradient
```css
background: linear-gradient(135deg, #22c55e 0%, #14b8a6 50%, #3b82f6 100%);
```
**Usage**: Hero sections, primary CTAs, brand elements

#### Secondary Gradient
```css
background: linear-gradient(135deg, #a855f7 0%, #3b82f6 50%, #14b8a6 100%);
```
**Usage**: Secondary sections, accent elements

#### Text Gradient
```css
background: linear-gradient(135deg, #22c55e, #14b8a6, #3b82f6);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
```
**Usage**: Headlines, brand text, special emphasis

## Typography

### Font Families

- **Display Font**: `Poppins` - Used for headings and brand elements
- **Body Font**: `Inter` - Used for body text and UI elements
- **Fallback**: `system-ui, sans-serif`

### Typography Scale

#### Headings
- **H1**: `text-4xl md:text-6xl lg:text-7xl` (36px → 60px → 72px)
- **H2**: `text-3xl md:text-4xl lg:text-5xl` (30px → 36px → 48px)
- **H3**: `text-2xl md:text-3xl lg:text-4xl` (24px → 30px → 36px)
- **H4**: `text-xl md:text-2xl` (20px → 24px)
- **H5**: `text-lg md:text-xl` (18px → 20px)
- **H6**: `text-base md:text-lg` (16px → 18px)

#### Body Text
- **Large**: `text-xl` (20px)
- **Regular**: `text-base` (16px)
- **Small**: `text-sm` (14px)
- **Extra Small**: `text-xs` (12px)

### Font Weights
- **Light**: `font-light` (300)
- **Regular**: `font-normal` (400)
- **Medium**: `font-medium` (500)
- **Semibold**: `font-semibold` (600)
- **Bold**: `font-bold` (700)
- **Extra Bold**: `font-extrabold` (800)

## Spacing System

We follow Tailwind's 4px-based spacing scale:

- **xs**: `0.5rem` (8px)
- **sm**: `1rem` (16px)
- **md**: `1.5rem` (24px)
- **lg**: `2rem` (32px)
- **xl**: `3rem` (48px)
- **2xl**: `4rem` (64px)
- **3xl**: `6rem` (96px)

### Layout Containers
- **Container**: Max-width responsive container with auto margins
- **Section Padding**: `py-20 lg:py-32` for major sections
- **Card Padding**: `p-6 lg:p-8` for card components

## Components

### Buttons

#### Primary Button
```html
<button class="bg-gradient-to-r from-primary-500 to-secondary-500 text-white px-6 py-3 rounded-lg font-medium transition-all duration-300 hover:shadow-lg hover:scale-105">
  Button Text
</button>
```

#### Secondary Button
```html
<button class="border-2 border-primary-500 text-primary-600 px-6 py-3 rounded-lg font-medium hover:bg-primary-500 hover:text-white transition-all duration-300">
  Button Text
</button>
```

#### Ghost Button
```html
<button class="text-primary-600 px-6 py-3 rounded-lg font-medium hover:bg-primary-50 transition-all duration-300">
  Button Text
</button>
```

### Cards

#### Standard Card
```html
<div class="bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 overflow-hidden">
  <div class="p-8">
    <!-- Card content -->
  </div>
</div>
```

#### Gradient Border Card
```html
<div class="bg-white rounded-2xl shadow-lg overflow-hidden">
  <div class="h-2 bg-gradient-to-r from-primary-500 to-secondary-500"></div>
  <div class="p-8">
    <!-- Card content -->
  </div>
</div>
```

### Navigation

#### Nav Link
```html
<a href="#" class="px-4 py-2.5 rounded-lg font-medium text-gray-700 hover:text-primary-600 hover:bg-gray-50 transition-all duration-200 flex items-center space-x-2">
  <i class="fas fa-icon"></i>
  <span>Link Text</span>
</a>
```

#### Active Nav Link
```html
<a href="#" class="bg-gradient-to-r from-primary-500 to-secondary-500 text-white shadow-md px-4 py-2.5 rounded-lg font-medium flex items-center space-x-2">
  <i class="fas fa-icon"></i>
  <span>Link Text</span>
</a>
```

## Animations & Effects

### Transitions
- **Fast**: `150ms cubic-bezier(0.4, 0, 0.2, 1)`
- **Normal**: `300ms cubic-bezier(0.4, 0, 0.2, 1)`
- **Slow**: `500ms cubic-bezier(0.4, 0, 0.2, 1)`

### Custom Animations

#### Fade In
```css
@keyframes fadeIn {
  0% { opacity: 0; transform: translateY(10px); }
  100% { opacity: 1; transform: translateY(0); }
}
```

#### Bounce Gentle
```css
@keyframes bounceGentle {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-5px); }
}
```

#### Float
```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}
```

### Glass Effects

#### Glass Morphism
```css
.glass-effect {
  background: rgba(255, 255, 255, 0.25);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.18);
}
```

## Responsive Design

### Breakpoints
- **sm**: `640px` - Small devices
- **md**: `768px` - Medium devices
- **lg**: `1024px` - Large devices
- **xl**: `1280px` - Extra large devices
- **2xl**: `1536px` - 2X large devices

### Mobile-First Approach
Always design for mobile first, then enhance for larger screens:

```html
<div class="text-2xl md:text-4xl lg:text-6xl">
  Responsive Text
</div>
```

## Accessibility

### Focus States
All interactive elements should have visible focus states:
```css
.focus-ring:focus {
  outline: 2px solid #22c55e;
  outline-offset: 2px;
}
```

### Color Contrast
- **Text on white**: Minimum AA compliance (4.5:1)
- **Text on colored backgrounds**: Always test contrast ratios
- **Interactive elements**: Clear visual hierarchy

### Screen Reader Support
```html
<span class="sr-only">Screen reader only text</span>
```

## Usage Guidelines

### Do's
✅ Use the defined color palette consistently
✅ Maintain proper spacing and typography hierarchy  
✅ Test all components on mobile devices
✅ Ensure adequate color contrast for accessibility
✅ Use gradients sparingly for impact
✅ Follow the component patterns for consistency

### Don'ts
❌ Don't use colors outside the defined palette
❌ Don't mix multiple gradients in one section
❌ Don't use tiny font sizes (below 14px)
❌ Don't ignore responsive breakpoints
❌ Don't remove focus states
❌ Don't use pure black (#000) for text

## Implementation

### CSS Custom Properties
```css
:root {
  --gradient-primary: linear-gradient(135deg, #22c55e 0%, #14b8a6 50%, #3b82f6 100%);
  --gradient-secondary: linear-gradient(135deg, #a855f7 0%, #3b82f6 50%, #14b8a6 100%);
  --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-normal: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
}
```

### Tailwind Configuration
The design system is configured in the base template with custom color definitions and animations through Tailwind's configuration object.

## Performance Considerations

### Optimization Techniques
- Use `will-change` property for elements that will animate
- Prefer CSS transforms over changing layout properties
- Use `backdrop-filter` with caution (check browser support)
- Optimize images and use modern formats (WebP, AVIF)
- Lazy load images and heavy content

### Loading States
Provide visual feedback during loading:
```html
<div class="loading-skeleton h-4 bg-gray-200 rounded animate-pulse"></div>
```

## Brand Voice

The design system should convey:
- **Professional**: Clean, organized, trustworthy
- **Innovative**: Modern, cutting-edge, forward-thinking  
- **Vibrant**: Energetic, growth-oriented, optimistic
- **Reliable**: Stable, consistent, dependable

## Maintenance

### Versioning
Track changes to the design system with semantic versioning:
- **Major**: Breaking changes to components or colors
- **Minor**: New components or enhancements
- **Patch**: Bug fixes or minor adjustments

### Updates
When updating the design system:
1. Document all changes in this file
2. Test across all breakpoints and browsers
3. Ensure accessibility compliance
4. Update component examples
5. Communicate changes to the development team

---

*Last updated: December 2024*
*Version: 1.0.0*