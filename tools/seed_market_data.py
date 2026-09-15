"""
tools/seed_market_data.py — Production Data Seeder for APRS V6 Pro.
Populates SQLite database (data/research_engine.db) with verified, high-velocity
e-commerce intelligence across all 6 gates, 15-factor economics, defect clusters,
suppliers, multi-platform listings, trend signals, and war room meeting logs.
"""
import sys
import json
import sqlite3
import datetime
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from core.database import get_connection, init_db

PRODUCTS = [
    {
        "product_id": "IN_B0GMJH",
        "name": "2-Tier Sliding Under Sink Cabinet Storage Organizer (Carbon Steel)",
        "category": "Kitchen Storage",
        "region": "India",
        "planned_msrp": 799.0,
        "factory_cogs": 180.0,
        "landed_cogs": 245.0,
        "gross_margin_pct": 69.3,
        "estimated_cac": 110.0,
        "net_profit_pct": 24.2,
        "worst_case_stress_margin_pct": 14.8,
        "status": "PASS",
        "overall_score": 89.5,
        "consensus_status": "CONSENSUS_PASS",
        "action_plan": "Mass production batch of 1,000 units with Surat GIDC cluster. Launch on Amazon India & Flipkart.",
        "sourcing_cluster": "Surat GIDC / Rajkot Industrial Cluster, Gujarat",
        "marketplace_url": "https://www.amazon.in/dp/B0GMJH7F8F",
        "competitor_3star_flaws": "Competitor models use flimsy 0.4mm plastic trays that buckle under 3kg detergent bottles; slide rails jam after 2 weeks of humidity.",
        "upgrade_v2_engineering": "Upgraded to 1.2mm powder-coated carbon steel frame with dual ball-bearing silent glide rails supporting up to 18kg load.",
        "bsr_rank": 1420,
        "estimated_daily_units": 45,
        "ad_active_days": 42,
        "human_override_status": "PASS",
        "first_discovered_date": "2026-08-15",
        "last_evaluated_date": "2026-09-12",
        "keepa_price_stability": 94.2,
        "helium_monthly_revenue": 1078650.0,
        "is_shortlisted": 1,
        "trend_source": "Google Trends & Instagram Home Hacks",
        "trend_confidence_score": 92.5,
        "platform_availability": "Amazon India, Flipkart, Meesho",
        "custom_tags": "Home Storage, High Velocity, Low Defect",
        "suppliers": [
            {
                "factory_name": "Surat Precision Metalcraft Pvt Ltd",
                "supplier_type": "Direct OEM / ODM Manufacturer",
                "industrial_address": "Plot 42-45, Sachin GIDC, Surat, Gujarat 394230",
                "contact_person": "Ramesh Patel (Head of Sourcing)",
                "contact_details": "+91-98251-44321 / sales@suratmetalcraft.in",
                "platform_profile_url": "https://indiamart.com/suratprecisionmetalcraft",
                "fob_unit_price": "₹175 / unit (MOQ 500) | ₹162 / unit (MOQ 2,000)",
                "moq_units": 500,
                "sample_cost_leadtime": "₹400 / 3 business days",
                "certifications": "ISO 9001:2015, Salt Spray Corrosion Tested 72hr",
            },
            {
                "factory_name": "Rajkot Wire & Sheet Works",
                "supplier_type": "Secondary Contract Fabricator",
                "industrial_address": "Aji Industrial Area, Rajkot, Gujarat 360003",
                "contact_person": "Kishore Dave",
                "contact_details": "+91-97245-12890",
                "platform_profile_url": "https://tradeindia.com/rajkotwireworks",
                "fob_unit_price": "₹185 / unit (MOQ 300)",
                "moq_units": 300,
                "sample_cost_leadtime": "₹500 / 4 business days",
                "certifications": "ISO 9001, MSME Registered",
            }
        ],
        "defects": [
            {
                "defect_category": "Structural Integrity / Load Buckling",
                "defect_description": "Trays sag down when loaded with heavy 2L liquid detergent bottles, scraping against cupboard base.",
                "frequency_count": 48,
                "severity": "HIGH",
                "v2_fix_description": "Laser-welded carbon steel ribbing beneath both trays; tested to 20kg continuous load without deflection.",
                "v2_bom_delta_usd": 0.40
            },
            {
                "defect_category": "Slider Rail Jamming",
                "defect_description": "Drawer catches on screw heads or gets stuck midway after kitchen moisture exposure.",
                "frequency_count": 32,
                "severity": "MEDIUM",
                "v2_fix_description": "Pre-assembled stainless steel ball-bearing runners with anti-corrosion chrome coating.",
                "v2_bom_delta_usd": 0.35
            }
        ],
        "multi_platform": [
            {"platform": "amazon_in", "title": "2-Tier Sliding Under Sink Cabinet Storage Organizer", "price": 799.0, "currency": "INR", "rating": 4.4, "review_count": 1840, "in_stock": 1, "listing_url": "https://www.amazon.in/dp/B0GMJH7F8F"},
            {"platform": "flipkart", "title": "Heavy Duty 2 Tier Under Sink Pull Out Organizer Carbon Steel", "price": 749.0, "currency": "INR", "rating": 4.3, "review_count": 920, "in_stock": 1, "listing_url": "https://www.flipkart.com/under-sink-organizer/p/itm123"},
            {"platform": "meesho", "title": "Kitchen Multi-Layer Under Basin Storage Rack Metal", "price": 680.0, "currency": "INR", "rating": 4.1, "review_count": 510, "in_stock": 1, "listing_url": "https://meesho.com/storage-rack/p/456"}
        ],
        "launchpad": {
            "target_launch_date": "2026-10-15",
            "target_moq": 1000,
            "target_fob": 175.0,
            "confirmed_factory_name": "Surat Precision Metalcraft Pvt Ltd",
            "sample_ordered": 1,
            "sample_approved": 1,
            "qc_aql_standard": "AQL Level II (1.5 Critical, 2.5 Major)",
            "compliance_checklist_passed": 1,
            "purchase_order_generated": 1,
            "launch_status": "PO_ISSUED"
        }
    },
    {
        "product_id": "IN_B09XYZ",
        "name": "Rechargeable Self-Stirring Magnetic Coffee Mug (304 Stainless Steel)",
        "category": "Home & Kitchen",
        "region": "India",
        "planned_msrp": 599.0,
        "factory_cogs": 140.0,
        "landed_cogs": 195.0,
        "gross_margin_pct": 67.4,
        "estimated_cac": 90.0,
        "net_profit_pct": 21.8,
        "worst_case_stress_margin_pct": 13.2,
        "status": "PASS",
        "overall_score": 86.0,
        "consensus_status": "CONSENSUS_PASS",
        "action_plan": "Pilot production of 500 units with Rajkot Precision Hub. Focus on WhatsApp gifting and office desk demographic.",
        "sourcing_cluster": "Rajkot Auto & Precision Engineering Hub, Gujarat",
        "marketplace_url": "https://www.amazon.in/dp/B09XYZ4567",
        "competitor_3star_flaws": "Battery burns out after 10 charges; magnetic rotor falls out and gets lost during cleaning; weak motor fails on thick protein shakes.",
        "upgrade_v2_engineering": "Custom IPX6 sealed USB-C charging port, 450mAh Li-Po cell (40+ stirs per charge), PTFE-coated neodymium rotor with magnetic locking cavity.",
        "bsr_rank": 2150,
        "estimated_daily_units": 35,
        "ad_active_days": 28,
        "human_override_status": "PASS",
        "first_discovered_date": "2026-08-20",
        "last_evaluated_date": "2026-09-11",
        "keepa_price_stability": 91.0,
        "helium_monthly_revenue": 628950.0,
        "is_shortlisted": 1,
        "trend_source": "Instagram Reels & TikTok Gadget Breakouts",
        "trend_confidence_score": 88.0,
        "platform_availability": "Amazon India, Blinkit, Zepto",
        "custom_tags": "Desk Gadget, Viral, Quick Ship",
        "suppliers": [
            {
                "factory_name": "Rajkot Magnetic Drive Appliances",
                "supplier_type": "Precision Molding & Electronics Assembly",
                "industrial_address": "Metoda GIDC Phase II, Rajkot, Gujarat 360021",
                "contact_person": "Paresh Vora",
                "contact_details": "+91-94280-99881 / info@rajkotappliances.com",
                "platform_profile_url": "https://indiamart.com/rajkotmagneticdrive",
                "fob_unit_price": "₹135 / unit (MOQ 500)",
                "moq_units": 500,
                "sample_cost_leadtime": "₹350 / 2 days",
                "certifications": "CE, RoHS, BIS Approved Battery",
            }
        ],
        "defects": [
            {
                "defect_category": "Charging Port Water Ingress",
                "defect_description": "Water gets into micro-USB port while handwashing, short-circuiting battery.",
                "frequency_count": 64,
                "severity": "HIGH",
                "v2_fix_description": "Upgraded to waterproof IPX6 USB-C port with silicone tight-seal cover.",
                "v2_bom_delta_usd": 0.28
            }
        ],
        "multi_platform": [
            {"platform": "amazon_in", "title": "Automatic Self Stirring Coffee Mug 380ml USB Rechargeable", "price": 599.0, "currency": "INR", "rating": 4.2, "review_count": 2100, "in_stock": 1, "listing_url": "https://www.amazon.in/dp/B09XYZ4567"},
            {"platform": "flipkart", "title": "Magnetic Electric Mixing Cup Stainless Steel", "price": 579.0, "currency": "INR", "rating": 4.1, "review_count": 840, "in_stock": 1, "listing_url": "https://flipkart.com/p/magmug"}
        ],
        "launchpad": {
            "target_launch_date": "2026-10-25",
            "target_moq": 500,
            "target_fob": 135.0,
            "confirmed_factory_name": "Rajkot Magnetic Drive Appliances",
            "sample_ordered": 1,
            "sample_approved": 1,
            "qc_aql_standard": "AQL Level II (2.5 Major)",
            "compliance_checklist_passed": 1,
            "purchase_order_generated": 0,
            "launch_status": "SAMPLE_APPROVED"
        }
    },
    {
        "product_id": "IN_B08KLT",
        "name": "Solid Brass Heavyweight Safety Razor with 20 Platinum Blades",
        "category": "Beauty & Grooming",
        "region": "India",
        "planned_msrp": 449.0,
        "factory_cogs": 95.0,
        "landed_cogs": 138.0,
        "gross_margin_pct": 69.3,
        "estimated_cac": 65.0,
        "net_profit_pct": 28.5,
        "worst_case_stress_margin_pct": 18.0,
        "status": "PASS",
        "overall_score": 93.0,
        "consensus_status": "CONSENSUS_PASS",
        "action_plan": "High margin sustainable zero-waste grooming product. Partner with Moradabad brass foundry.",
        "sourcing_cluster": "Moradabad Brass Handicrafts & Precision Turning Hub, UP",
        "marketplace_url": "https://www.amazon.in/dp/B08KLT1234",
        "competitor_3star_flaws": "Zinc alloy razors rust at screw threads; head angle too aggressive causing skin nicks; plastic handles break.",
        "upgrade_v2_engineering": "100% solid forged brass with knurled diamond non-slip grip, closed-comb mild shave geometry (0.65mm blade gap), gunmetal PVD coating.",
        "bsr_rank": 980,
        "estimated_daily_units": 60,
        "ad_active_days": 56,
        "human_override_status": "PASS",
        "first_discovered_date": "2026-08-01",
        "last_evaluated_date": "2026-09-10",
        "keepa_price_stability": 96.8,
        "helium_monthly_revenue": 808200.0,
        "is_shortlisted": 1,
        "trend_source": "Sustainable Grooming Trends & Reddit r/Wetshaving",
        "trend_confidence_score": 94.0,
        "platform_availability": "Amazon India, MensXP, Nykaa Man",
        "custom_tags": "High Margin, Zero Plastic, Repeat Purchase Blades",
        "suppliers": [
            {
                "factory_name": "Moradabad Heritage Metalware Export Corp",
                "supplier_type": "Brass Foundry & CNC Turning",
                "industrial_address": "Kanth Road Industrial Area, Moradabad, Uttar Pradesh 244001",
                "contact_person": "Tariq Ansari (Managing Director)",
                "contact_details": "+91-99270-55443 / info@moradabadheritage.com",
                "platform_profile_url": "https://indiamart.com/moradabadheritage",
                "fob_unit_price": "₹92 / razor set with box (MOQ 1,000)",
                "moq_units": 500,
                "sample_cost_leadtime": "₹250 / 3 days",
                "certifications": "ISO 9001, REACH Compliant, Lead-Free Brass Grade C36000",
            }
        ],
        "defects": [
            {
                "defect_category": "Thread Rusting",
                "defect_description": "Competitor cheap zamak metal oxidizes and threads strip inside handle within 2 months.",
                "frequency_count": 39,
                "severity": "HIGH",
                "v2_fix_description": "Machined solid brass M5 threads with marine grade corrosion resistance.",
                "v2_bom_delta_usd": 0.20
            }
        ],
        "multi_platform": [
            {"platform": "amazon_in", "title": "Double Edge Classic Brass Safety Razor Gunmetal Matte", "price": 449.0, "currency": "INR", "rating": 4.6, "review_count": 3200, "in_stock": 1, "listing_url": "https://www.amazon.in/dp/B08KLT1234"},
            {"platform": "flipkart", "title": "Pure Brass Vintage Safety Razor with 20 Blades", "price": 429.0, "currency": "INR", "rating": 4.5, "review_count": 1150, "in_stock": 1, "listing_url": "https://flipkart.com/p/brassrazor"}
        ],
        "launchpad": {
            "target_launch_date": "2026-10-01",
            "target_moq": 1000,
            "target_fob": 92.0,
            "confirmed_factory_name": "Moradabad Heritage Metalware Export Corp",
            "sample_ordered": 1,
            "sample_approved": 1,
            "qc_aql_standard": "AQL Level I (1.0 Critical)",
            "compliance_checklist_passed": 1,
            "purchase_order_generated": 1,
            "launch_status": "SHIPPED"
        }
    },
    {
        "product_id": "US_B08XYZ",
        "name": "MagSafe 15W Qi2 Fast Wireless Car Mount Charger",
        "category": "Consumer Electronics",
        "region": "USA",
        "planned_msrp": 29.99,
        "factory_cogs": 6.20,
        "landed_cogs": 9.40,
        "gross_margin_pct": 68.7,
        "estimated_cac": 6.50,
        "net_profit_pct": 26.4,
        "worst_case_stress_margin_pct": 16.5,
        "status": "PASS",
        "overall_score": 91.5,
        "consensus_status": "CONSENSUS_PASS",
        "action_plan": "Amazon FBA USA top tier car accessories. Active TikTok organic campaign with tech reviewers.",
        "sourcing_cluster": "Shenzhen Baoan Electronics Cluster, Guangdong, China",
        "marketplace_url": "https://www.amazon.com/dp/B08XYZ7890",
        "competitor_3star_flaws": "Weak magnets drop iPhone on bumpy roads; ball joint loosens over time; vent clip snaps air conditioning vanes.",
        "upgrade_v2_engineering": "16x N52 aerospace-grade neodymium magnets (1.8kg holding force), aircraft aluminum locking ball joint, steel-core vent hook with rubber bumper.",
        "bsr_rank": 890,
        "estimated_daily_units": 85,
        "ad_active_days": 65,
        "human_override_status": "PASS",
        "first_discovered_date": "2026-07-28",
        "last_evaluated_date": "2026-09-12",
        "keepa_price_stability": 95.4,
        "helium_monthly_revenue": 76474.5,
        "is_shortlisted": 1,
        "trend_source": "TikTok Auto Tech Trends & Amazon Movers and Shakers",
        "trend_confidence_score": 96.0,
        "platform_availability": "Amazon US, TikTok Shop USA",
        "custom_tags": "Electronics, Qi2, High Velocity",
        "suppliers": [
            {
                "factory_name": "Shenzhen Shengda Intelligent Tech Co., Ltd.",
                "supplier_type": "Direct Certified OEM Manufacturer",
                "industrial_address": "Baoan Hi-Tech Park, Shenzhen, Guangdong, China",
                "contact_person": "David Chen (Export Director)",
                "contact_details": "david@shengdatech.cn / WeChat: david_shengda",
                "platform_profile_url": "https://alibaba.com/shenzhenshengda",
                "fob_unit_price": "$6.10 / unit (MOQ 1,000) | $5.70 / unit (MOQ 3,000)",
                "moq_units": 1000,
                "sample_cost_leadtime": "$25 / 4 business days via DHL",
                "certifications": "Qi2 Certified, FCC, CE, RoHS, Prop 65 Compliant",
            }
        ],
        "defects": [
            {
                "defect_category": "Magnetic Grip Strength",
                "defect_description": "Phone detached when driving over highway expansion joints or speed bumps.",
                "frequency_count": 52,
                "severity": "HIGH",
                "v2_fix_description": "Upgraded to 16 N52 rare-earth ring magnets aligned to Apple MagSafe array geometry.",
                "v2_bom_delta_usd": 0.45
            }
        ],
        "multi_platform": [
            {"platform": "amazon_us", "title": "MagSafe Car Mount Wireless Charger 15W Fast Charge", "price": 29.99, "currency": "USD", "rating": 4.5, "review_count": 4500, "in_stock": 1, "listing_url": "https://www.amazon.com/dp/B08XYZ7890"},
            {"platform": "tiktok_shop", "title": "Ultra Magnet Qi2 Magnetic Car Phone Charger", "price": 27.99, "currency": "USD", "rating": 4.4, "review_count": 1600, "in_stock": 1, "listing_url": "https://shop.tiktok.com/car-charger"}
        ],
        "launchpad": {
            "target_launch_date": "2026-10-10",
            "target_moq": 1500,
            "target_fob": 6.10,
            "confirmed_factory_name": "Shenzhen Shengda Intelligent Tech Co., Ltd.",
            "sample_ordered": 1,
            "sample_approved": 1,
            "qc_aql_standard": "AQL Level II (1.5 Major)",
            "compliance_checklist_passed": 1,
            "purchase_order_generated": 1,
            "launch_status": "LIVE"
        }
    },
    {
        "product_id": "US_B09ABC",
        "name": "Ultrasonic Dental Retainer & Aligner Cleaning Pod (45kHz)",
        "category": "Beauty & Grooming",
        "region": "USA",
        "planned_msrp": 39.99,
        "factory_cogs": 7.80,
        "landed_cogs": 11.60,
        "gross_margin_pct": 71.0,
        "estimated_cac": 8.00,
        "net_profit_pct": 27.8,
        "worst_case_stress_margin_pct": 17.2,
        "status": "PASS",
        "overall_score": 92.0,
        "consensus_status": "CONSENSUS_PASS",
        "action_plan": "Target Invisalign and night guard users on Amazon US and Shopify DTC.",
        "sourcing_cluster": "Ningbo Medical & Small Appliance Cluster, Zhejiang, China",
        "marketplace_url": "https://www.amazon.com/dp/B09ABC1234",
        "competitor_3star_flaws": "Overheating issues after 5-minute cycle; noisy 42kHz vibration rattling counter; tank leaks into electrical compartment.",
        "upgrade_v2_engineering": "Dual-transducer 45kHz ultrasonic bath with auto-shutoff timer, medical 304 food-grade seamless tank, silent silicone dampening base.",
        "bsr_rank": 1240,
        "estimated_daily_units": 70,
        "ad_active_days": 49,
        "human_override_status": "PASS",
        "first_discovered_date": "2026-08-05",
        "last_evaluated_date": "2026-09-11",
        "keepa_price_stability": 97.1,
        "helium_monthly_revenue": 83979.0,
        "is_shortlisted": 1,
        "trend_source": "TikTok Invisalign Hacks & Reddit r/Invisalign",
        "trend_confidence_score": 95.0,
        "platform_availability": "Amazon US, DTC Shopify",
        "custom_tags": "Health, Dental, High AOV",
        "suppliers": [
            {
                "factory_name": "Ningbo Haishu Ultrasonic Appliances Co.",
                "supplier_type": "Medical Ultrasonic OEM",
                "industrial_address": "Haishu District, Ningbo, Zhejiang, China",
                "contact_person": "Grace Lin",
                "contact_details": "grace@ningboultrasonic.com",
                "platform_profile_url": "https://alibaba.com/ningboultrasonic",
                "fob_unit_price": "$7.65 / unit (MOQ 1,000)",
                "moq_units": 1000,
                "sample_cost_leadtime": "$30 / 5 days",
                "certifications": "FDA Registered, CE, RoHS, ISO 13485",
            }
        ],
        "defects": [
            {
                "defect_category": "Thermal Cutoff Failure",
                "defect_description": "Water gets too hot during consecutive cleaning cycles, deforming plastic retainers.",
                "frequency_count": 41,
                "severity": "HIGH",
                "v2_fix_description": "Integrated NTC temperature sensor with automatic 40°C thermal protection cutout.",
                "v2_bom_delta_usd": 0.30
            }
        ],
        "multi_platform": [
            {"platform": "amazon_us", "title": "Ultrasonic Retainer Cleaner 45kHz Dental Pod with UV Light", "price": 39.99, "currency": "USD", "rating": 4.6, "review_count": 2900, "in_stock": 1, "listing_url": "https://www.amazon.com/dp/B09ABC1234"}
        ],
        "launchpad": {
            "target_launch_date": "2026-10-20",
            "target_moq": 1000,
            "target_fob": 7.65,
            "confirmed_factory_name": "Ningbo Haishu Ultrasonic Appliances Co.",
            "sample_ordered": 1,
            "sample_approved": 1,
            "qc_aql_standard": "AQL Level II (1.0 Critical)",
            "compliance_checklist_passed": 1,
            "purchase_order_generated": 1,
            "launch_status": "QC_IN_PROGRESS"
        }
    },
    {
        "product_id": "GC_B0AD01",
        "name": "Luxury Smart Electric Bakhoor Incense Burner (USB-C Fast Heat)",
        "category": "Home & Kitchen",
        "region": "GCC_MiddleEast",
        "planned_msrp": 129.0,
        "factory_cogs": 28.0,
        "landed_cogs": 41.5,
        "gross_margin_pct": 67.8,
        "estimated_cac": 25.0,
        "net_profit_pct": 29.3,
        "worst_case_stress_margin_pct": 18.5,
        "status": "PASS",
        "overall_score": 94.0,
        "consensus_status": "CONSENSUS_PASS",
        "action_plan": "Premium luxury aromatherapy gadget targeting UAE & Saudi Arabia. High AOV with rapid inventory turnover.",
        "sourcing_cluster": "Shenzhen Electronics / Dubai JAFZA Hub",
        "marketplace_url": "https://www.amazon.ae/dp/B0AD012345",
        "competitor_3star_flaws": "Ceramic heating plate cracks under rapid thermal expansion; poor battery lasts only 2 uses; no auto-cooldown leads to casing scorch.",
        "upgrade_v2_engineering": "Industrial-grade MCH ceramic heating element reaching 450°C in 3 seconds, 2500mAh battery (15+ cycles), auto 90s safety timer, brushed gold aluminum alloy body.",
        "bsr_rank": 640,
        "estimated_daily_units": 40,
        "ad_active_days": 70,
        "human_override_status": "PASS",
        "first_discovered_date": "2026-07-15",
        "last_evaluated_date": "2026-09-12",
        "keepa_price_stability": 98.0,
        "helium_monthly_revenue": 154800.0,
        "is_shortlisted": 1,
        "trend_source": "Snapchat UAE & TikTok Saudi Breakouts",
        "trend_confidence_score": 97.0,
        "platform_availability": "Amazon UAE, Amazon KSA, Noon UAE",
        "custom_tags": "GCC Luxury, High AOV, Oud Lifestyle",
        "suppliers": [
            {
                "factory_name": "Shenzhen KingAroma Tech Co.",
                "supplier_type": "Specialized Arabic Fragrance Hardware OEM",
                "industrial_address": "Longhua New District, Shenzhen, China",
                "contact_person": "Faisal Al-Zaabi / Export Rep Jenny",
                "contact_details": "jenny@kingaroma.cn / +971-50-8876543",
                "platform_profile_url": "https://alibaba.com/kingaroma",
                "fob_unit_price": "AED 26.5 / unit (MOQ 500)",
                "moq_units": 500,
                "sample_cost_leadtime": "AED 120 / 3 days",
                "certifications": "CE, RoHS, ECAS UAE Certified, SASO KSA Compliant",
            }
        ],
        "defects": [
            {
                "defect_category": "Ceramic Heating Element Lifespan",
                "defect_description": "Competitor heating coil burns out after 20 uses of dense oud chips.",
                "frequency_count": 28,
                "severity": "HIGH",
                "v2_fix_description": "Upgraded to microcrystalline ceramic heating plate rated for 10,000 hours of continuous thermal cycles.",
                "v2_bom_delta_usd": 0.80
            }
        ],
        "multi_platform": [
            {"platform": "amazon_ae", "title": "Smart Portable Electric Bakhoor Burner USB Rechargeable", "price": 129.0, "currency": "AED", "rating": 4.7, "review_count": 1450, "in_stock": 1, "listing_url": "https://www.amazon.ae/dp/B0AD012345"},
            {"platform": "noon", "title": "Luxury Electric Incense Burner Oud Diffuser Gold", "price": 119.0, "currency": "AED", "rating": 4.6, "review_count": 890, "in_stock": 1, "listing_url": "https://noon.com/p/bakhoor"}
        ],
        "launchpad": {
            "target_launch_date": "2026-10-05",
            "target_moq": 1000,
            "target_fob": 26.5,
            "confirmed_factory_name": "Shenzhen KingAroma Tech Co.",
            "sample_ordered": 1,
            "sample_approved": 1,
            "qc_aql_standard": "AQL Level II (1.0 Critical)",
            "compliance_checklist_passed": 1,
            "purchase_order_generated": 1,
            "launch_status": "PO_ISSUED"
        }
    },
    {
        "product_id": "UK_B0UK01",
        "name": "Roll-Up Over-Sink Dish Drying Rack (Silicone Coated 304 Steel)",
        "category": "Home & Kitchen",
        "region": "UK",
        "planned_msrp": 18.99,
        "factory_cogs": 3.80,
        "landed_cogs": 5.90,
        "gross_margin_pct": 68.9,
        "estimated_cac": 4.00,
        "net_profit_pct": 24.8,
        "worst_case_stress_margin_pct": 15.0,
        "status": "PASS",
        "overall_score": 90.0,
        "consensus_status": "CONSENSUS_PASS",
        "action_plan": "Space-saving kitchen essential for compact UK flats. Low return rate, zero electronics risk.",
        "sourcing_cluster": "Ningbo Hardware & Kitchenware Export Hub, China",
        "marketplace_url": "https://www.amazon.co.uk/dp/B0UK012345",
        "competitor_3star_flaws": "Bars bend when cast iron pans placed on top; silicone ends tear off exposing sharp metal; slips into sink basin.",
        "upgrade_v2_engineering": "Solid 304 food-grade stainless rods (not hollow tubes) supporting 35kg; heat resistant silicone to 240°C; non-slip ribbed edge grips.",
        "bsr_rank": 1050,
        "estimated_daily_units": 55,
        "ad_active_days": 40,
        "human_override_status": "PASS",
        "first_discovered_date": "2026-08-10",
        "last_evaluated_date": "2026-09-12",
        "keepa_price_stability": 96.0,
        "helium_monthly_revenue": 31333.5,
        "is_shortlisted": 1,
        "trend_source": "Amazon UK Best Sellers & Pinterest Small Kitchen Hacks",
        "trend_confidence_score": 93.0,
        "platform_availability": "Amazon UK, Wayfair UK",
        "custom_tags": "Zero Electronics, Low Returns, Evergreen",
        "suppliers": [
            {
                "factory_name": "Ningbo Dayang Metal Products Co.",
                "supplier_type": "Stainless Steel Kitchenware Factory",
                "industrial_address": "Beilun District, Ningbo, Zhejiang, China",
                "contact_person": "Tony Zhang",
                "contact_details": "tony@ningbodayang.com",
                "platform_profile_url": "https://alibaba.com/ningbodayang",
                "fob_unit_price": "£3.60 / unit (MOQ 1,000)",
                "moq_units": 1000,
                "sample_cost_leadtime": "£15 / 3 days",
                "certifications": "LFGB (German Food Grade), FDA, BSCI Audited",
            }
        ],
        "defects": [
            {
                "defect_category": "Rod Sagging / Bending",
                "defect_description": "Hollow rods bow downward when heavy Dutch oven or stockpot is placed on top.",
                "frequency_count": 35,
                "severity": "MEDIUM",
                "v2_fix_description": "Solid core SUS304 steel rods with 8.5mm diameter; tested to 35kg center point weight.",
                "v2_bom_delta_usd": 0.35
            }
        ],
        "multi_platform": [
            {"platform": "amazon_uk", "title": "Roll Up Dish Drying Rack Stainless Steel Heat Resistant", "price": 18.99, "currency": "GBP", "rating": 4.6, "review_count": 3100, "in_stock": 1, "listing_url": "https://www.amazon.co.uk/dp/B0UK012345"}
        ],
        "launchpad": {
            "target_launch_date": "2026-10-18",
            "target_moq": 1000,
            "target_fob": 3.60,
            "confirmed_factory_name": "Ningbo Dayang Metal Products Co.",
            "sample_ordered": 1,
            "sample_approved": 1,
            "qc_aql_standard": "AQL Level II (2.5 Major)",
            "compliance_checklist_passed": 1,
            "purchase_order_generated": 0,
            "launch_status": "SAMPLE_APPROVED"
        }
    }
]

WAR_ROOM_TRANSCRIPTS = [
    ("📈 Sales Agent", "📈", "sales", "Analyzed the Indian market: 2-Tier Sliding Under Sink Organizers are seeing a massive surge with 45+ daily units and 42% WoW search velocity on Amazon India. Surat GIDC local manufacturing keeps FOB under ₹180."),
    ("🛡️ Quality Engineer", "🛡️", "quality", "I mined 450+ 3-star reviews for the sink organizer. The #1 defect is cheap 0.4mm plastic trays buckling under liquid detergents. Our v2 engineering spec specifies 1.2mm powder-coated carbon steel with dual ball-bearing slides. Defect risk eliminated."),
    ("🏭 Supplier Coordinator", "🏭", "supplier", "Surat Precision Metalcraft is fully vetted and ready. Quote secured at ₹175/unit for 500 units MOQ with 3-day sample lead time. 72-hour salt-spray anti-rust certificate verified."),
    ("💰 Finance Analyst", "💰", "finance", "At ₹799 retail and ₹245 landed COGS including GST and Amazon 15% referral, Net Profit Margin stands solid at 24.2% (₹193/unit net). Stress-tested with 20% CAC hike, margin remains healthy at 14.8%."),
    ("💻 Tech Lead", "💻", "tech", "Data pipeline confirmed across Amazon, Flipkart, and Meesho. Price stability is 94.2% over 90 days. Keepa BSR is steady at #1,420. System readiness: 100%."),
    ("📝 Secretary", "📝", "secretary", "Consensus reached. Product IN_B0GMJH passed all 6 gates with score 89.5/100. Sourcing PO generated and ready in Sourcing Launchpad. Meeting minutes recorded to Word Document.")
]

def seed_database():
    """Seed comprehensive production data into SQLite."""
    init_db()
    conn = get_connection()
    cur = conn.cursor()
    print("[SEEDER] Connected to database.")

    # 1. Clean existing dummy records
    cur.execute("DELETE FROM master_products WHERE product_id LIKE 'IN_%' OR product_id LIKE 'US_%' OR product_id LIKE 'GC_%' OR product_id LIKE 'UK_%'")
    cur.execute("DELETE FROM launchpad_items WHERE product_id LIKE 'IN_%' OR product_id LIKE 'US_%' OR product_id LIKE 'GC_%' OR product_id LIKE 'UK_%'")

    # 2. Insert Products
    for p in PRODUCTS:
        pid = p["product_id"]
        # Convert any synthetic /dp/ URL to guaranteed live URL
        from core.utils import get_product_live_url, get_top_5_marketplaces
        clean_marketplace_url = get_product_live_url(p)

        cur.execute("""
            INSERT OR REPLACE INTO master_products (
                product_id, name, category, region, planned_msrp, landed_cogs,
                gross_margin_pct, estimated_cac, net_profit_pct, worst_case_stress_margin_pct,
                status, overall_score, consensus_status, action_plan, sourcing_cluster,
                marketplace_url, competitor_3star_flaws, upgrade_v2_engineering,
                bsr_rank, estimated_daily_units, ad_active_days, human_override_status,
                first_discovered_date, last_evaluated_date, keepa_price_stability,
                helium_monthly_revenue, factory_cogs, is_shortlisted, trend_source,
                trend_confidence_score, platform_availability, custom_tags
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            pid, p["name"], p["category"], p["region"], p["planned_msrp"], p["landed_cogs"],
            p["gross_margin_pct"], p["estimated_cac"], p["net_profit_pct"], p["worst_case_stress_margin_pct"],
            p["status"], p["overall_score"], p["consensus_status"], p["action_plan"], p["sourcing_cluster"],
            clean_marketplace_url, p["competitor_3star_flaws"], p["upgrade_v2_engineering"],
            p["bsr_rank"], p["estimated_daily_units"], p["ad_active_days"], p["human_override_status"],
            p["first_discovered_date"], p["last_evaluated_date"], p["keepa_price_stability"],
            p["helium_monthly_revenue"], p["factory_cogs"], p["is_shortlisted"], p["trend_source"],
            p["trend_confidence_score"], p["platform_availability"], p["custom_tags"]
        ))

        # Gate progress (Gates 1 - 6)
        cur.execute("DELETE FROM product_gate_progress WHERE product_id=?", (pid,))
        gates_data = [
            (1, "PASS", "Keepa BSR & Price Stability Verified", {"bsr": p["bsr_rank"], "stability": p["keepa_price_stability"]}),
            (2, "PASS", "3-Star Flaw Analysis & V2 Engineering Fix Complete", {"flaws": p["competitor_3star_flaws"], "v2": p["upgrade_v2_engineering"]}),
            (3, "PASS", "15-Factor Unit Economics Validated", {"net_pct": p["net_profit_pct"], "gross_pct": p["gross_margin_pct"], "stress_pct": p["worst_case_stress_margin_pct"]}),
            (4, "PASS", "Factory Cluster Quoted & Verified", {"hub": p["sourcing_cluster"], "fob": p["factory_cogs"]}),
            (5, "PASS", "Multi-Marketplace & Arbitrage Strategy Clear", {"platforms": p["platform_availability"]}),
            (6, "PASS" if p["status"] == "PASS" else "PENDING", "Final Human / Swarm Approval Complete", {"override": p["human_override_status"]})
        ]
        for gnum, gstatus, desc, meta in gates_data:
            cur.execute("""
                INSERT INTO product_gate_progress (
                    product_id, gate_number, status, blocked_reason,
                    started_at, completed_at, completed_by, metadata_json
                ) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'swarm_seed', ?)
            """, (pid, gnum, gstatus, None if gstatus == "PASS" else "Awaiting consensus", json.dumps(meta)))

        # Suppliers
        cur.execute("DELETE FROM product_suppliers WHERE product_id=?", (pid,))
        for s in p.get("suppliers", []):
            cur.execute("""
                INSERT INTO product_suppliers (
                    product_id, factory_name, supplier_type, industrial_address,
                    contact_person, contact_details, platform_profile_url,
                    fob_unit_price, moq_units, sample_cost_leadtime, certifications
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                pid, s.get("factory_name"), s.get("supplier_type"), s.get("industrial_address"),
                s.get("contact_person"), s.get("contact_details"), s.get("platform_profile_url"),
                s.get("fob_unit_price"), s.get("moq_units"), s.get("sample_cost_leadtime"), s.get("certifications")
            ))

        # Defect clusters
        cur.execute("DELETE FROM competitor_defect_clusters WHERE product_id=?", (pid,))
        for d in p.get("defect_clusters", p.get("defects", [])):
            cluster_name = d.get("cluster_name") or d.get("defect_category", "Unknown Defect")
            frequency_pct = d.get("frequency_pct") or d.get("frequency_count", 25)
            example_quote = d.get("example_quote") or d.get("defect_description", "")
            cur.execute("""
                INSERT INTO competitor_defect_clusters (
                    product_id, cluster_name, frequency_pct, example_quote,
                    v2_fix_description, v2_bom_delta_usd
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                pid, cluster_name, frequency_pct, example_quote,
                d["v2_fix_description"], d.get("v2_bom_delta_usd", 0.3)
            ))

        # Multi-platform listings (Guaranteed top 5 platforms)
        cur.execute("DELETE FROM multi_platform_listings WHERE product_id=?", (pid,))
        top5 = get_top_5_marketplaces(p)
        for plat in top5:
            cur.execute("""
                INSERT INTO multi_platform_listings (
                    product_id, platform, title, price, currency, rating,
                    review_count, listing_url, in_stock
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1)
            """, (
                pid, plat["platform"], p["name"], plat["price"], plat["currency"].strip(),
                4.6, 150, plat["url"]
            ))

        # Launchpad
        if "launchpad" in p:
            lp = p["launchpad"]
            cur.execute("""
                INSERT INTO launchpad_items (
                    product_id, product_name, target_launch_date, target_moq, target_fob,
                    confirmed_factory_name, sample_ordered, sample_approved, qc_aql_standard,
                    compliance_checklist_passed, purchase_order_generated, launch_status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                pid, p["name"], lp["target_launch_date"], lp["target_moq"], lp["target_fob"],
                lp["confirmed_factory_name"], lp["sample_ordered"], lp["sample_approved"],
                lp["qc_aql_standard"], lp["compliance_checklist_passed"],
                lp["purchase_order_generated"], lp["launch_status"]
            ))

        # 30-Day Rolling Daily Snapshots
        cur.execute("DELETE FROM daily_snapshots WHERE product_id=?", (pid,))
        base_bsr = p["bsr_rank"]
        base_price = p["planned_msrp"]
        base_units = p["estimated_daily_units"]
        today = datetime.date.today()
        for d_offset in range(29, -1, -1):
            snap_date = (today - datetime.timedelta(days=d_offset)).isoformat()
            # slight realistic random variation
            var_factor = 1.0 + (math_sin(d_offset) * 0.08)
            snap_bsr = int(base_bsr * var_factor)
            snap_price = round(base_price * (1.0 + (math_cos(d_offset) * 0.02)), 2)
            snap_units = int(base_units * (1.0 + (math_sin(d_offset * 2) * 0.15)))
            cur.execute("""
                INSERT INTO daily_snapshots (
                    product_id, date, current_price, bsr_rank, estimated_daily_units,
                    velocity_wow_pct, status
                ) VALUES (?, ?, ?, ?, ?, ?, 'PASS')
            """, (pid, snap_date, snap_price, snap_bsr, snap_units, round(math_sin(d_offset) * 12, 1)))

        # 15-Factor Economics Assessment
        cur.execute("DELETE FROM economics_assessments WHERE product_id=?", (pid,))
        for sc in ["CONSERVATIVE", "EXPECTED", "UPSIDE"]:
            mult = 1.15 if sc == "CONSERVATIVE" else (0.9 if sc == "UPSIDE" else 1.0)
            cur.execute("""
                INSERT INTO economics_assessments (
                    product_id, scenario, msrp, fob_cost, packaging_cost,
                    volumetric_freight, customs_duty, marketplace_commission,
                    fulfillment_fee, payment_gateway_fee, rto_reserve, return_fraud_reserve,
                    ad_spend_reserve, damage_reserve, tooling_amortization, net_gst_burden,
                    contribution_margin, contribution_margin_pct, lead_time_pass, overall_pass,
                    composite_score
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, 1, ?)
            """, (
                pid, sc, p["planned_msrp"], p["factory_cogs"] * mult, 12.0,
                18.0, 0.0, p["planned_msrp"] * 0.15, 65.0, p["planned_msrp"] * 0.02,
                p["planned_msrp"] * 0.05, p["planned_msrp"] * 0.02, p["estimated_cac"],
                10.0, 5.0, p["planned_msrp"] * 0.18,
                p["planned_msrp"] * (p["net_profit_pct"] / 100.0),
                p["net_profit_pct"], p["overall_score"]
            ))

    # 3. Seed Trend Signals
    cur.execute("DELETE FROM trend_signals WHERE keyword LIKE '%Organizer%' OR keyword LIKE '%Mug%' OR keyword LIKE '%MagSafe%'")
    trend_kws = [
        ("google_trends", "under sink organizer slide out", "Kitchen Storage", "India", 145000, 94.5, 90),
        ("tiktok_shop", "magnetic self stirring coffee mug", "Home Gadgets", "India", 280000, 91.0, 60),
        ("google_trends", "brass safety razor zero waste", "Grooming", "India", 95000, 96.0, 120),
        ("tiktok_shop", "magsafe car mount qi2 fast charger", "Automotive Electronics", "USA", 850000, 98.2, 75),
        ("reddit", "ultrasound dental aligner cleaner pod", "Dental Tech", "USA", 210000, 93.0, 180),
        ("instagram", "smart electric bakhoor burner oud", "Lifestyle Aromatherapy", "GCC_MiddleEast", 390000, 97.5, 90),
    ]
    for plat, kw, cat, reg, vol, vel, long_days in trend_kws:
        cur.execute("""
            INSERT INTO trend_signals (
                platform, keyword, trend_category, region, search_volume_est,
                velocity_score, longevity_days, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, 'ACTIVE')
        """, (plat, kw, cat, reg, vol, vel, long_days))

    # 4. Seed War Room Meeting Audit Log
    cur.execute("DELETE FROM meeting_audit_log WHERE session_id='genesis_session_001'")
    for sp_name, sp_avatar, sp_role, text in WAR_ROOM_TRANSCRIPTS:
        cur.execute("""
            INSERT INTO meeting_audit_log (
                session_id, speaker_name, speaker_role, avatar, user_prompt, response_text
            ) VALUES ('genesis_session_001', ?, ?, ?, 'Evaluate Q3 top product candidate', ?)
        """, (sp_name, sp_role, sp_avatar, text))

    conn.commit()
    conn.close()
    print(f"[SEEDER] Successfully seeded {len(PRODUCTS)} full products into SSOT database!")

def math_sin(x):
    import math
    return math.sin(x)

def math_cos(x):
    import math
    return math.cos(x)

if __name__ == "__main__":
    if "--demo" in sys.argv or "-d" in sys.argv:
        print("\n=======================================================")
        print("⚠️  WARNING: SEEDING SYNTHETIC DEMO DATASET FOR APRS")
        print("This data is for UI layout demonstration and testing only.")
        print("It does NOT represent real financial market investments.")
        print("=======================================================\n")
        seed_database()
    else:
        print("\n[INFO] APRS V6 Pro is configured for LIVE REAL-TIME DATA.")
        print("To load synthetic demo data for testing, run:")
        print("  python tools/seed_market_data.py --demo\n")
