"""
Algorithm 11: Safety Demonstration (Python)
Case: Concurrent Data Integrity (Race Condition)

This example demonstrates the difference between standard AI-generated code
and code governed by Algorithm 11 principles.

Focus: 
- Property 6 (Constraint): Preventing race conditions.
- Property 10 (Support): Implementing robust synchronization primitives.
"""

import asyncio

# --- SCENARIO 1: STANDARD AI OUTPUT (UNSAFE) ---
# Most LLMs generate this code because it looks syntactically correct,
# but it fails to account for asynchronous context switching.
class UnsafeWallet:
    def __init__(self):
        self.balance = 0

    async def deposit(self, amount: int):
        current_balance = self.balance
        # Simulating an I/O operation (e.g., Database or API latency)
        await asyncio.sleep(0.01) 
        self.balance = current_balance + amount

# --- SCENARIO 2: ALGORITHM 11 GOVERNED OUTPUT (SAFE) ---
# A11 forces the AI to identify the "State Integrity" constraint (Property 6)
# and provide a reliable synchronization mechanism (Property 10).
class SecureWallet:
    def __init__(self):
        self.balance = 0
        # Property 10 (Support): Initializing the synchronization primitive
        self._lock = asyncio.Lock()

    async def deposit(self, amount: int):
        # Property 6 (Constraint): Entry into the critical section
        async with self._lock:
            current_balance = self.balance
            # Simulating the same I/O latency
            await asyncio.sleep(0.01)
            self.balance = current_balance + amount
            # The lock ensures that no other task overwrites the state during the 'await'

async def run_battle_test(wallet_name, wallet):
    print(f"--- Testing: {wallet_name} ---")
    
    # Executing 100 concurrent deposit tasks of 1 unit each
    tasks = [wallet.deposit(1) for _ in range(100)]
    await asyncio.gather(*tasks)
    
    expected = 100
    actual = wallet.balance
    
    print(f"Final Balance: {actual} (Expected: {expected})")
    if actual != expected:
        print(f"Status: ❌ FAILED - Data loss of {expected - actual} units detected.\n")
    else:
        print("Status: ✅ SUCCESS - Integrity verified.\n")

async def main():
    print("ALGORITHM 11: INTEGRITY BATTLE TEST\n" + "="*35 + "\n")
    
    # 1. Test Standard AI approach
    await run_battle_test("Standard AI Implementation", UnsafeWallet())
    
    # 2. Test Algorithm 11 approach
    await run_battle_test("Algorithm 11 Implementation", SecureWallet())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
