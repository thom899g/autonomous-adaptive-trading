import os
from dataclasses import dataclass
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass
class ExchangeConfig:
    """Exchange-specific configuration"""
    name: str
    api_key: Optional[str] = None
    api_secret: Optional[str] = None
    sandbox: bool = True
    rate_limit: int = 1000

@dataclass
class ModelConfig:
    """Machine learning model configuration"""
    retrain_interval_hours: int = 24
    validation_window_days: int = 30
    feature_window_days: int = 60
    prediction_horizon_hours: int = 6

@dataclass
class RiskConfig:
    """Risk management configuration"""
    max_position_size_percent: float = 2.0
    max_portfolio_risk_percent: float = 10.0
    stop_loss_percent: float = 5.0
    take_profit_percent: float = 15.0
    max_concurrent_trades: int = 5

class TradingConfig:
    """Main trading system configuration"""
    
    def __init__(self):
        # Firebase Configuration
        self.firebase_credentials_path = os.getenv('FIREBASE_CREDENTIALS_PATH', 'firebase_credentials.json')
        self.firestore_collection = os.getenv('FIRESTORE_COLLECTION', 'trading_system')
        
        # Exchange Configuration
        self.exchanges: Dict[str, ExchangeConfig] = {
            'binance': ExchangeConfig(
                name='binance',
                api_key=os.getenv('BINANCE_API_KEY'),
                api_secret=os.getenv('BINANCE_API_SECRET'),
                sandbox=os.getenv('BINANCE_SANDBOX', 'true').lower() == 'true'
            ),
            'coinbase': ExchangeConfig(
                name='coinbase',
                api_key=os.getenv('COINBASE_API_KEY'),
                api_secret=os.getenv('COINBASE_API_SECRET')
            )
        }
        
        # Model Configuration
        self.model = ModelConfig()
        
        # Risk Configuration
        self.risk = RiskConfig()
        
        # Trading Parameters
        self.symbols = os.getenv('TRADING_SYMBOLS', 'BTC/USDT,ETH/USDT').split(',')
        self.primary_timeframe = os.getenv('PRIMARY_TIMEFRAME', '1h')
        self.min_volume_usd = float(os.getenv('MIN_VOLUME_USD', '1000000'))
        
        # System Parameters
        self.data_collection_interval = int(os.getenv('DATA_COLLECTION_INTERVAL', '300'))
        self.signal_generation_interval = int(os.getenv('SIGNAL_GENERATION_INTERVAL', '900'))
        self.max